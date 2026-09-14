import importlib
import unittest
from importlib.metadata import entry_points


class NoOpenTester(unittest.TestCase):
    """zcmds owns `open`; zcmds_win32 must not install a colliding script."""

    def test_open_console_script_not_registered(self) -> None:
        scripts = {
            ep.name
            for ep in entry_points(group="console_scripts")
            if ep.dist is not None
            and ep.dist.name.replace("-", "_").lower() == "zcmds_win32"
        }
        self.assertNotIn("open", scripts)

    def test_open_module_removed(self) -> None:
        with self.assertRaises(ModuleNotFoundError):
            importlib.import_module("zcmds_win32.cmds.open")


if __name__ == "__main__":
    unittest.main()
