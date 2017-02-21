SublimeLinter-contrib-livecodelint
================================

[![Build Status](https://travis-ci.org/trevordevore/sublimelinter-contrib-livecodelint.svg?branch=master)](https://travis-ci.org/trevordevore/sublimelinter-contrib-livecodelint)

This linter plugin for [SublimeLinter][docs] provides an interface for checking syntax for [LiveCode][livecode-homepage]. It will be used with files that are using the “LiveCode” syntax in Sublime Text.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### LiveCode Package Installation

You will need to install the [LiveCode Package][livecode-package] before installing the linter.

### LiveCode server executable installation
Before using this plugin, you must ensure that a LiveCode Server executable is installed on your system. To install a version of LiveCode server, do the following:

1. Download the version of `livecode-community-server` from [http://downloads.livecode.com](http://downloads.livecode.com) that you would like to use to check syntax. This plugin has been tested with LiveCode 8.
2. Move the executable to a folder where SublimeLinter will be able to access it. For example, on OS X you might move the `livecode-community-server` file to the `/usr/local/bin` folder. DO NOT RENAME the executable.
3. Configure settings as described below.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, livecodelint provides its own settings. You configure these settings in the SublimeLinter User Settings file.

|Setting|Description|
|:------|:----------|
|livecode-server-path|The full path to the `livecode-community-server` file on your computer|
|explicitvars|Set to true to have the linter ensure that variables are declared|

To add these settings use the `Tools > SublimeLinter > Open User Settings` menu to open the user settings file. Add the following configuration text to the "linters" section:

```
"livecodelint": {
    "@disable": false,
    "args": [],
    "excludes": [],
    "explicitvars": true,
    "livecode-server-path": "/usr/local/bin/livecode-community-server"
}
```

After adding the above settings your user settings will look something like this:

```
"user": {
        "debug": false,
        "delay": 0.25,
        "error_color": "D02000",
        "gutter_theme": "Packages/SublimeLinter/gutter-themes/Default/Default.gutter-theme",
        "gutter_theme_excludes": [],
        "lint_mode": "background",
        "linters": {
            "flake8": {
                "@disable": false,
                "args": [],
                "builtins": "",
                "excludes": [],
                "executable": "",
                "ignore": "",
                "jobs": "1",
                "max-complexity": -1,
                "max-line-length": null,
                "select": "",
                "show-code": false
            },
            "livecodelint": {
                "@disable": false,
                "args": [],
                "excludes": [],
                "explicitvars": true,
                "livecode-server-path": "/usr/local/bin/livecode-community-server"
            }
        },
        ...
```

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `livecodelint`. Among the entries you should see `SublimeLinter-contrib-livecodelint`. If that entry is not highlighted, use the keyboard or mouse to select it.

### Manual Installation

If you would like to manually install the plugin then place the `SublimeLinter-contrib-livecodelint ` folder in the Sublime Text user package folder. On OS X that folder is `~/Library/Application Support/Sublime Text 3/Packages`.

## Notes

The livecodelint.lc file was taken from the [LiveCode language package for Atom][livecode-atom]

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[livecode-homepage]: https://livecode.org
[LiveCode]: https://github.com/trevordevore/livecode-sublimetext
[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[livecode-package]: https://github.com/trevordevore/livecode-sublimetext
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[livecode-atom]: https://github.com/peter-b/atom-language-livecode
