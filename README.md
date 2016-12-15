SublimeLinter-contrib-livecodelint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-livecodelint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-livecodelint)

This linter plugin for [SublimeLinter][docs] provides an interface to [livecodelint](__linter_homepage__). It will be used with files that have the “__livecode__” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### LiveCode Package Installation

You will need to install the [LiveCode Package][livecode-package] before installing the linter.

### Linter installation
Before using this plugin, you must ensure that `livecodelint` is installed on your system. To install `livecodelint`, do the following:

1. Download the a version of `livecode-community-server` from [http://downloads.livecode.com](http://downloads.livecode.com) and store it somewhere on your computer. You will point the linter to the file in the settings.
2. Download the files in this repository and place the folder in the Sublime Text 3 user Packages folder. 
3. Configure settings as described below.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-livecodelint provides its own settings. You configure these settings in the SublimeLinter User Settings file.

|Setting|Description|
|:------|:----------|
|livecode-server-path|The full path to the `livecode-community-server` file on your computer|
|explicitvars|Set to true to have the linter ensure that variables are declared|

After adding these two settings to your user settings file the `livecodelint` section should look something like this:

```
"livecodelint": {
    "@disable": false,
    "args": [],
    "excludes": [],
    "explicitvars": true,
    "livecode-server-path": "/usr/local/bin/livecode-community-server"
}
```

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

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[livecode-package]: https://github.com/trevordevore/livecode-sublimetext
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
[livecode-atom]: https://github.com/peter-b/atom-language-livecode
