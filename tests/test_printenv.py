import io
import os
import unittest
from contextlib import redirect_stdout
from importlib.metadata import entry_points
from unittest.mock import patch


def _run_printenv(env: dict[str, str]) -> tuple[int, str]:
    from zcmds_win32.cmds import printenv

    buf = io.StringIO()
    with patch.dict(os.environ, env, clear=True), redirect_stdout(buf):
        rtn = printenv.main()
    return rtn, buf.getvalue()


class PrintenvTester(unittest.TestCase):
    def test_prints_sorted_vars_then_path_block(self) -> None:
        """Variables are sorted case-insensitively and PATH is listed last, one entry per line."""
        env = {"ZED": "2", "ALPHA": "1", "PATH": os.pathsep.join(["p1", "p2"])}
        rtn, out = _run_printenv(env)
        self.assertEqual(rtn, 0)
        self.assertEqual(
            out.splitlines(), ["ALPHA=1", "ZED=2", "PATH:", "  p1", "  p2"]
        )

    def test_path_unset_does_not_crash(self) -> None:
        """A missing PATH prints the other variables and no PATH block."""
        rtn, out = _run_printenv({"ALPHA": "1"})
        self.assertEqual(rtn, 0)
        self.assertEqual(out.splitlines(), ["ALPHA=1"])

    def test_console_script_registered(self) -> None:
        """The installed zcmds_win32 distribution exposes the printenv console script."""
        scripts = {
            ep.name: ep.value
            for ep in entry_points(group="console_scripts")
            if ep.dist is not None
            and ep.dist.name.replace("-", "_").lower() == "zcmds_win32"
        }
        self.assertEqual(scripts.get("printenv"), "zcmds_win32.cmds.printenv:main")


if __name__ == "__main__":
    unittest.main()
