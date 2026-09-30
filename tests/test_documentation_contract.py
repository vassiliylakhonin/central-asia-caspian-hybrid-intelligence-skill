"""Exercise documentation checks against missing disclosures and stale routing."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.egg-info', '.pytest_cache'))
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)

    def validate(self, script='scripts/validate.py'):
        env = dict(os.environ, SKIP_SITE_LINK_CHECK='1')
        return subprocess.run([sys.executable, script], cwd=self.root, capture_output=True, text=True, env=env, timeout=30)

    def test_current_documentation_passes(self):
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_real_use_disclosure_fails(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text().replace('no public, attributable real-use record', 'a public record').replace('No public, attributable real-use record', 'A public record'))
        self.assertNotEqual(self.validate().returncode, 0)

    def test_old_current_uk_source_fails(self):
        path = self.root / 'SKILL.md'
        path.write_text(path.read_text() + '\n- Where to verify: OFSI consolidated list.\n')
        result = self.validate('scripts/validate_runtime_contract.py')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('UK Sanctions List', result.stderr)

    def test_mixed_memo_downgrade_fails(self):
        path = self.root / 'SKILL.md'
        path.write_text(path.read_text() + '\nDowngrade evidence mode to `mixed`.\n')
        self.assertNotEqual(self.validate('scripts/validate_runtime_contract.py').returncode, 0)

    def test_missing_regional_reference_fails(self):
        path = self.root / 'SKILL.md'
        path.write_text(path.read_text().replace('docs/risk-archetypes.md', 'docs/unrelated.md'))
        self.assertNotEqual(self.validate('scripts/validate_runtime_contract.py').returncode, 0)

    def test_stale_example_counts_fail(self):
        path = self.root / 'examples/fintech-sanctions-routing.md'
        path.write_text(path.read_text().replace('reasoning-only', 'illustrative source packet'))
        self.assertNotEqual(self.validate().returncode, 0)


if __name__ == '__main__':
    unittest.main()
