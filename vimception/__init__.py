"""
Custom exception hook.
"""

import os
import subprocess
import sys
import traceback


def excepthook(exctype, value, tb):
    """Custom excepthook."""

    sys.__excepthook__(exctype, value, tb)

    frame_summary = traceback.extract_tb(tb, limit=-1)
    if not frame_summary:
        return
    frame_summary = frame_summary[-1]

    filename = frame_summary.filename
    if filename == "<stdin>":
        return

    command = [
        os.environ.get("EDITOR", "vim"),
        "-c",
        f"call cursor({frame_summary.lineno}, 0)",
        "--",
        filename,
    ]

    subprocess.call(command)
