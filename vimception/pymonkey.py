"""
Monkey patching.
"""


def pymonkey_argparse(argv):
    """Argument patcher."""

    import argparse

    parser = argparse.ArgumentParser()

    return parser.parse_known_args(argv)


def pymonkey_patch(mod, args):
    """Module patcher."""

    # hack since sys is not included here...
    if mod.__name__ != 'logging':
        return
    mod = mod.sys

    import vimception

    mod.excepthook, mod.__excepthook__ = vimception.excepthook, mod.excepthook
