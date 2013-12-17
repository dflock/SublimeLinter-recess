#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Duncan Lock
# Copyright (c) 2013 Duncan Lock
#
# License: MIT
#

"""This module exports the Recess plugin class."""

from SublimeLinter.lint import Linter, highlight
import os


class Recess(Linter):

    """Provides an interface to recess."""

    syntax = 'less'
    executable = 'recess'
    regex = r'''(?xi)
        ^.+?:                        # filename
        (?P<line>\d+?|undefined):    # line
        (?P<message>.*)              # message
        $'''
    tempfile_suffix = 'less'
    default_type = highlight.WARNING

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method so that general errors that do not have
        a line number can be placed at the beginning of the code - and
        so I can further parse message to extract near, if available.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line == 'undefined' and message:
            line = 0
            col = 0

        if '"' in message:
            near = message.split('"')[1::2]

        return match, line, col, error, warning, message, near

    def cmd(self):
        """Return a tuple with the command line to execute.

        We override this method so we can properly set the --includePath
        parameter.
        """

        include_path = '--includePath={}'.format(os.path.dirname(self.filename))

        result = [
            'recess',
            '--format=compact',
            '--stripColors=true',
            '--noSummary=true',
            '--strictPropertyOrder=false',
            '--compile=false',
            '--compress=false',
            include_path]

        return result
