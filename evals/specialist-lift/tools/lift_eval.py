#!/usr/bin/env python3
"""Prepare frozen three-condition prompts, export blind packets, and score receipts."""
import argparse
import random
import shutil
import sys
from datetime import date
from pathlib import Path

from integrity import (CONDITIONS, PROTOCOL, REFERENCES, build_report, check_prepared,
                       digest, families, item_ids, load, slug, write)

SUITE = Path(__file__).resolve().parent.parent
ROOT = SUITE.parents[1]
RUBRIC = SUITE / 'rubric.md'


def prepare(args):
    slug(args.run_id)
    rubric = RUBRIC.read_text()
    items = item_ids(rubric)
    manifest = {'protocol': PROTOCOL, 'run_id': args.run_id,
                'prepared_on': date.today().isoformat(), 'model': args.model,
                'model_family': args.model_family.lower(), 'judge_model': args.judge_model,
                'judge_family': args.judge_family.lower(), 'seed': args.seed,
                'generation_settings': {'tools': 'none', 'output_budget': args.output_budget,
                                        'temperature': args.temperature},
                'rubric_items': items, 'rubric_sha256': digest(RUBRIC)}
    families(manifest)
    run = SUITE / 'runs' / args.run_id
    if run.exists():
        if not args.force or any((run / name).exists() for name in ('outputs', 'scores.json', 'report.json', 'judge-receipt.json')):
            raise ValueError('run exists; never overwrite generated or scored runs; choose a new id')
        shutil.rmtree(run)
    run.mkdir(parents=True)
    # Snapshots include all regional references used by the rubric, not just the root skill.
    inputs = {'inputs/rubric.md': RUBRIC, 'inputs/horizontal.md': Path(args.horizontal_skill)}
    inputs.update({f'inputs/vertical/{relative}': ROOT / relative for relative in REFERENCES})
    for relative, source in inputs.items():
        target = run / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    manifest['input_sha256'] = {relative: digest(run / relative) for relative in inputs}
    horizontal = (run / 'inputs/horizontal.md').read_text()
    vertical = '\n\n---\n\n'.join(f'# Reference: {relative}\n\n{(run / f"inputs/vertical/{relative}").read_text()}' for relative in REFERENCES)
    rng = random.Random(args.seed)
    entries, blinding = [], {}
    for path in sorted((SUITE / 'cases').glob('*.json')):
        case = load(path)
        case_id = slug(case['id'])
        if case_id in blinding:
            raise ValueError('duplicate case id')
        question = f"# Question\n\n{case['question']}\n\n# Decision context\n\n{case['decision_context']}"
        hashes = {}
        for condition in CONDITIONS:
            parts = ([horizontal] if condition in 'BC' else []) + ([vertical] if condition == 'C' else []) + [question]
            target = run / 'prompts' / f'{case_id}__condition_{condition}.txt'
            target.parent.mkdir(exist_ok=True)
            target.write_text('\n\n---\n\n'.join(parts))
            hashes[condition] = digest(target)
        target = run / 'inputs/cases' / path.name
        target.parent.mkdir(exist_ok=True)
        shutil.copyfile(path, target)
        manifest['input_sha256'][target.relative_to(run).as_posix()] = digest(target)
        shuffled = list(CONDITIONS)
        rng.shuffle(shuffled)
        blinding[case_id] = {f'output_{index + 1}': condition for index, condition in enumerate(shuffled)}
        entries.append({'case_id': case_id, 'archetype': case['archetype'],
                        'negative_control': bool(case.get('negative_control', False)), 'prompt_sha256': hashes})
    manifest['cases'] = entries
    write(run / 'manifest.json', manifest)
    write(run / 'blinding-key.json', blinding)
    check_prepared(run)
    print(f'prepared {len(entries)} cases x 3 conditions; no outputs generated')


def export_judge(args):
    run = SUITE / 'runs' / slug(args.run_id)
    manifest = check_prepared(run)
    if (run / 'judge-receipt.json').exists():
        raise ValueError('judge export is frozen; use a new run rather than replace it')
    mapping = load(run / 'blinding-key.json')
    hashes, packets = {}, {}
    for entry in manifest['cases']:
        case_id = entry['case_id']
        packets[case_id] = {}
        for anonymous, condition in mapping[case_id].items():
            path = run / 'outputs' / f'{case_id}__condition_{condition}.md'
            if not path.is_file() or not path.read_text().strip():
                raise ValueError(f'missing or empty output: {path.name}')
            hashes[path.relative_to(run).as_posix()] = digest(path)
            packets[case_id][anonymous] = path.read_text()
    # The judge receives only judge/; no model IDs, conditions, manifest or blinding key.
    for case, outputs in packets.items():
        write(run / 'judge' / f'{case}.json', {'case_id': case, 'outputs': outputs,
              'rubric': (run / 'inputs/rubric.md').read_text(), 'score_format':
              {'output_1': {'S1': {'satisfied': True, 'rationale': 'Explain criterion match',
                                    'evidence': 'Verbatim span from this output'}}}})
    write(run / 'judge-receipt.json', {'manifest_sha256': digest(run / 'manifest.json'),
          'blinding_sha256': digest(run / 'blinding-key.json'), 'output_sha256': hashes})
    print('blind judge packets exported; commit receipts before judging')


def score(args):
    run = SUITE / 'runs' / slug(args.run_id)
    manifest = check_prepared(run)
    if digest(RUBRIC) != manifest['rubric_sha256']:
        raise ValueError('rubric changed after preparation; register a new run')
    report = build_report(run)
    write(run / 'report.json', report)
    print(f"mean C-over-B lift: {report['mean_lift_c_over_b']}; scope: {report['scope']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('run_id')
    for flag in ('model', 'model-family', 'judge-model', 'judge-family', 'horizontal-skill'):
        prep.add_argument('--' + flag, required=True)
    prep.add_argument('--seed', type=int, default=0)
    prep.add_argument('--output-budget', type=int, default=4096)
    prep.add_argument('--temperature', type=float, default=0)
    prep.add_argument('--force', action='store_true')
    prep.set_defaults(func=prepare)
    for command, function in (('judge', export_judge), ('score', score)):
        sub = commands.add_parser(command)
        sub.add_argument('run_id')
        sub.set_defaults(func=function)
    args = parser.parse_args()
    try:
        if getattr(args, 'output_budget', 1) <= 0:
            raise ValueError('output budget must be positive')
        args.func(args)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
