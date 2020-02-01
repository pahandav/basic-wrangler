# BASIC Wrangler

A BASIC program listing line renumberer/cruncher (aka, a minifier).

**_This program is currently in alpha testing._** It will probably break your program. The documentation is minimal. Things will change frequently.

## Purpose

The purpose of BASIC Wrangler is to allow you to write BASIC programs using labels in a dialect-agnostic way. It also combines and crunches lines to take up the least amount of space, thus saving you memory. It is designed to be able to work with almost any dialect of line numbered BASIC.

## Basic Usage

Type just `bw` to load the GUI. Type `bw -h` for CLI help. For more, check out [the Manual](docs/Manual.asc) in the docs directory.

## Some of the Planned Features

- [x] Built-in conversion from numbered listings routine
- [x] A GUI
- [x] Output to clipboard when pasting
- [ ] Preprocessor macros like includes and ifs
- [ ] Renaming variables
- [ ] Support for external tokenizers by accounting for how many bytes each token uses
- [x] Support for output to files that can be transferred directly into disk images

## Changelog

### 0.04.0 - 2020-01-28

- Added a lexer for tokenizing keywords.
- Added a native routine for conversion from numbered listings.
- Major documentation update.
- Added some more testing files.

### 0.03.0 - 2019-11-22

- Changed the BASIC definition and abbreviation routines to use YAML for the definitions.
- Changed to QBasic-style labeling.
- Fixed the DATA statement reformatter.
- Integrated helper scripts into main program with subcommands.
- Changed logging routine to output debug logs with duallog.
- Added seperate entry point scripts.

### 0.02.0 - 2019-10-27

- File mode with more command line arguments
- Paste mode now places output directly onto the clipboard so you can paste directly into emulators
- A basic GUI has been added
- Various minor fixes and refactoring

### 0.01.0 - 2019-10-24

- Initial release
