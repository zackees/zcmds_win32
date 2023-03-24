import os
import unittest
from pathlib import Path
from zcmds_win32.unix_tool_path import install

PROJECT_ROOT = Path(__file__).parent.parent

LS_GIT_BIN_PATH = PROJECT_ROOT / "zcmds_win32" / "git-bash-bin" / "ls.exe"


class GitBinInstallTester(unittest.TestCase):
    def test_install(self) -> None:
        """Tests that the download works."""
        install()
        self.assertTrue(os.path.exists(LS_GIT_BIN_PATH))


if __name__ == "__main__":
    unittest.main()
