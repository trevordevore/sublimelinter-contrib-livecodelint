#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Trevor DeVore
# Copyright (c) 2016 Trevor DeVore
#
# License: MIT
#

"""This module exports the Livecodelint plugin class."""
import os
from SublimeLinter.lint import Linter, util

class Livecodelint(Linter):
    """Provides an interface to livecodelint."""
    syntax = ('livecode')
    cmd = ['']
    executable = 'livecode-community-server'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = ''
    regex = r'(?P<line>\d+),(?P<col>\d+),(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

    """ Variables set by user """
    livecode_path = ''
    explicit_vars = False

    """ Store path to LiveCode script that acts as bridge between livecode community server and SublimeLinter """
    livecodelint_path = ''

    def __init__(self, view, syntax):
        """Initialize and load lc-community-server from settings if present."""
        Linter.__init__(self, view, syntax)

        self.livecode_path = self.get_view_settings().get('livecode-server-path')
        self.explicit_vars = self.get_view_settings().get('explicitvars')
        self.livecodelint_path =  os.path.dirname(__file__) + '/livecodelint.lc'

    def run(self, cmd, code):
        cmd = [self.livecode_path, self.livecodelint_path, '-scope=.source.livecodescript',
            '-explicitVariables=' + str(self.explicit_vars).lower()]
        return self.communicate(cmd, code)
