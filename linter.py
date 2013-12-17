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

from SublimeLinter.lint import Linter, util, highlight
import os


class Recess(Linter):

    """Provides an interface to recess."""

    syntax = 'less'
    cmd = 'recess --format compact --stripColors true --noSummary true --strictPropertyOrder false --includePath %s *' % '.'
    # executable = None
    regex = r'''(?xi)
        ^.+:                        # filename
        (?P<line>\d+|undefined):    # line
        (?P<message>.*)             # message
        $'''
    # multiline = False
    # line_col_base = (1, 1)
    tempfile_suffix = 'less'
    # error_stream = util.STREAM_STDOUT
    # selectors = {}
    # word_re = None
    # defaults = {
    #     '--includePath:': '.',
    # }
    # inline_settings = None
    # inline_overrides = None
    # comment_re = None
    default_type = highlight.WARNING

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method so that general errors that do not have
        a line number can be placed at the beginning of the code.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line == 'undefined' and message:
            line = 0
            col = 0

        if '"' in message:
            near = message.split('"')[1::2]

        return match, line, col, error, warning, message, near
