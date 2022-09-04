"""Custom exception hook."""

import os
import subprocess
import sys
import traceback
from pathlib import Path
from types import ModuleType, TracebackType
from typing import Type

EDITOR = os.environ.get("EDITOR", "vim")


def excepthook(exctype: Type[Exception], value: Exception, tb: TracebackType) -> None:
    """Custom excepthook."""

    sys.__excepthook__(exctype, value, tb)

    frame_summary = traceback.extract_tb(tb, limit=-1)
    if not frame_summary:
        return

    stack_summary = frame_summary[-1]
    if stack_summary.filename == "<stdin>":
        return

    path = Path(stack_summary.filename).expanduser()
    lineno = stack_summary.lineno or 0
    command = f"call cursor({lineno}, 0) | echomsg '{exctype.__name__}: {value}'"

    subprocess.call([EDITOR, "-c", command, "--", path.resolve()])


def replace_excepthook(module: ModuleType = sys) -> None:
    """Replace excepthook."""

    module.excepthook, module.__excepthook__ = excepthook, module.excepthook  # type: ignore
