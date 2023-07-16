import os
import unittest


class DigTester(unittest.TestCase):
    def test_dig_main(self) -> None:
        """Tests the ls command."""
        import zcmds_win32.cmds.dig

        zcmds_win32.cmds.dig.main()

    def test_dig_cmd(self) -> None:
        """Tests the ls command."""

        os.system("dig google.com")


if __name__ == "__main__":
    unittest.main()
