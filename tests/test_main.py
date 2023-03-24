import unittest


class MainTester(unittest.TestCase):
    def test_imports(self) -> None:
        """Tests the imports."""
        import zcmds_win32.cmds.fixvmmem
        import zcmds_win32.cmds.open
        import zcmds_win32.unix_tool_path
        import zcmds_win32._exec

    def test_ls(self) -> None:
        """Tests the ls command."""
        import zcmds_win32.cmds.ls

        zcmds_win32.cmds.ls.main()


if __name__ == "__main__":
    unittest.main()
