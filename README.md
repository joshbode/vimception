Vim Exceptions
--------------

Automatically jump to the line in Vim/Neovim where an exception was thrown
from a Python program.

Installation
============

Currently unpackaged - install in editable mode:

```sh
$ git clone https://github.com/joshbode/vimception.git
$ pip install -e vimception
```

Usage
=====

Add the following function to your shell environment file:

```sh
function vimception {
  AUTOWRAPT_BOOTSTRAP=vimception $*
}
```

Engage `vimception` for a script run directly via `python`:
```sh
$ vimception python somefile.py
```

Engage `vimception` for some entry-point script:
```sh
$ vimception pip ...
```
