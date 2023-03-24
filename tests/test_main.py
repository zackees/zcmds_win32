import unittest


class MainTester(unittest.TestCase):
    def test_imports(self) -> None:
        """Tests the imports."""
        import zcmds_win32.fixvmmem
        import zcmds_win32.open
        import zcmds_win32.unix_tool_path
        import zcmds_win32._exec

    def test_ls(self) -> None:
        """Tests the ls command."""
        import zcmds_win32.ls

        zcmds_win32.ls.main()


if __name__ == "__main__":
    unittest.main()
