import os
import unittest
from zcmds_win32.unix_tool_path import install
from zcmds_win32.settings import SRC_ROOT

LS_GIT_BIN_PATH = SRC_ROOT / "git-bash-bin" / "ls.exe"


class GitBinInstallTester(unittest.TestCase):
    def test_install(self) -> None:
        """Tests that the download works."""
        install()
        self.assertTrue(os.path.exists(LS_GIT_BIN_PATH), f"Could not find {LS_GIT_BIN_PATH}")


if __name__ == "__main__":
    unittest.main()
