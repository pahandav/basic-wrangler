# Changelog

## 0.7.0 - 2020-02-14

- Added tokenizers for Amiga ACE Compiler, Apple IIGS GSoft BASIC, and Acorn RISC OS.
- Replaced the logging library with loguru.
- The convert routine now extracts labels to an external file.
- Said file can be modified to replace the label names that are outputted by the conversion routine.
- This can be done to already converted files, as well.
- Single-sourced the version number.

## 0.6.0 - 2020-02-11

- Added Amstrad CPC, BBC Micro, Coleco ADAM, MSX, and Oric BASIC tokenizer rules.
- Updated the renumbering routine with a tokenizer. Labels no longer have to start with an underscore.
- Better Sinclair BASIC laziness features.
- Automatic LET and GOTO after THEN insertion for Sinclair BASIC.
- Conversely, it will no longer output LET or GOTO after THEN for other BASIC dialects in order to save space.

## 0.5.1 - 2020-02-05

- There's been a bunch of internal changes due to converting this to be installable by pip from PyPI. It should still work **_exactly_** the same, but some bugs might have slipped through.
- The leading zero on the middle of the version number is now gone.
- Now installable through pip.
- The Windows version is now 32-bit, as 64-bit was kind of overkill. The installer is now smaller as a result.

## 0.05.0 - 2020-02-01

- Added keywords for Apple /// Business BASIC, Color Computer BASIC, ZX81 BASIC, and ZX Spectrum BASIC.
- Changed the interface to specify BASIC type instead of using mutually exclusive groups.
- Added a handler for Commodore 8-bit BASIC upper/lowercase.
- Now only uses one entry point script.
- Added images to documentation and moved changelog out of main README.
- 64-bit Windows EXE version now available through pyinstaller.
- Added a custom icon.

## 0.04.0 - 2020-01-28

- Added a lexer for tokenizing keywords.
- Added a native routine for conversion from numbered listings.
- Major documentation update.
- Added some more testing files.

## 0.03.0 - 2019-11-22

- Changed the BASIC definition and abbreviation routines to use YAML for the definitions.
- Changed to QBasic-style labeling.
- Fixed the DATA statement reformatter.
- Integrated helper scripts into main program with subcommands.
- Changed logging routine to output debug logs with duallog.
- Added seperate entry point scripts.

## 0.02.0 - 2019-10-27

- File mode with more command line arguments
- Paste mode now places output directly onto the clipboard so you can paste directly into emulators
- A basic GUI has been added
- Various minor fixes and refactoring

## 0.01.0 - 2019-10-24

- Initial release
