#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Trevor DeVore
# Copyright (c) 2016-2018 Trevor DeVore
#
# License: MIT
#

"""This module exports the Livecodelint plugin class."""
import os
from SublimeLinter.lint import Linter


LIVECODE_SCRIPT = os.path.join(os.path.dirname(__file__), 'livecodelint.lc')


class Livecodelint(Linter):
    """Provides an interface to livecodelint."""

    cmd = ('livecode-community-server', LIVECODE_SCRIPT, '$args')
    regex = r'(?P<line>\d+),(?P<col>\d+),(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    word_re = None

    defaults = {
        'selector': 'source.livecode',
        '-scope=': '.source.livecodescript',
        '-explicitVariables=': False
    }
