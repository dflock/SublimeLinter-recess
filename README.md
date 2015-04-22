# PLEASE NOTE: Not available in Package Control, also: DOESN'T REALLY WORK

This isn't quite finished, which is why it's not available in Package Control.

One of the reasons that this plugin isn't finished, is that since writing this I've discovered that [recess](https://github.com/twitter/recess) is unmaintained.

In addition, recess returns output in a different format if there's a CSS/LESS syntax error, rather than a warning - it ignores its own `--format` parameter in this case.

Even worse is the fact that recess doesn't actually lint - **or even look at** - the actual less file. It compiles the less to css, then lints that - so the line numbers you get back only vaguely match the original less file and the messages are often not very relevant.

**All in all, I'm inclined to delete this repo - unless someone else want to take this on?**

SublimeLinter-recess
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [recess](https://github.com/twitter/recess). It will be used with files that have the “LESS” syntax.

## Installation

### Linter installation
Before installing this plugin, you must ensure that `recess` is installed on your system. To install `recess`, do the following:

1. Install [Node.js](http://nodejs.org/) and [npm](https://npmjs.org/).

1. Install `recess` by typing the following in a terminal:
    ```
    npm install recess -g
    ```

Now you can proceed to install the SublimeLinter-recess plugin.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `recess`. Among the entries you should see `SublimeLinter-recess`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Settings). For information on generic linter settings, please see [Linter Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Linter-Settings).


## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
