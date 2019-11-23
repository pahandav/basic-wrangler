# basic-wrangler

A BASIC program listing line renumberer/cruncher.

***This program is currently in alpha testing.*** It will probably break your program. The documentation is minimal. Things will change frequently.

## Purpose

The purpose of BASIC Wrangler is to allow you to write BASIC programs using labels in a dialect-agnostic way. It also combines and crunches lines to take up the least amount of space, thus saving you memory. It is designed to be able to work with almost any dialect of line numbered BASIC.

## Requirements

- Python 3 (any version of 3 should work, only tested with 3.7)
- pyperclip
- Gooey
- PyYAML
- duallog

You should run this before the first time you run the program:

```Batchfile
pip install pyperclip Gooey PyYAML duallog
```

## Usage

```Batchfile
bw <BASIC Type> <filename>
```

When run as `bwgui`, it will bring up the GUI.

The BASIC Type is the dialect of BASIC that you wish to use. You can find all the current definitions in [`basdefs.py`](basdefs.py).

When not in paste mode, it will output to `<filename-out>.bas` unless you specify an output file name with `-o`. You can then either transfer the file into a disk image or you can paste the code into an emulator if you used the paste mode.

### Extra Options

`-o <filename>` Set the output filename (If set, it will always output to a file, regardless of whether or not you also output to the clipboard)

`-p` Sets paste to clipboard mode (Certain dialects always output to a file)

`-l <maximum line number length>` Sets a non-default maximum BASIC line length

`-n <number to start numbering with>` Sets the line number to begin numbering with

`-i <number to increment lines by>` Sets the increment between BASIC lines

## Special Notes

The Commodore Amiga dialect is set up to use the ACE BASIC Compiler. Copy the .b file to a shared emulator directory, and run `bas -iO <filename minus the .b>` to compile it.

The RISC OS dialect needs to be tokenized to be runnable. To do this, copy the ,ffb file to a shared emulator directory, load it in RISC OS by shift-double-clicking it, and then save it back with F3.

The ZX81 and ZX Spectrum dialects are meant to be tokenized by the EightyOne emulator, but other tokenizers should be able to handle the output files.

## Writing Programs for BASIC Wrangler

- *Write one statement per line* unless you're doing something complicated with IF statements. A statement is whatever you would write up until you hit a colon to seperate statements.
- *Write with spaces where appropriate*. BASIC Wrangler will deal with the output spacing for you.
- You should write all BASIC keywords in **upper-case**.
- Labels **MUST** start with a letter or an _ (underscore) character, QBasic style. You must add a colon after the jump target label.
- To indicate a jump target, you should have the label on its own on the line directly preceding the jump target.
- For the ZX Spectrum, if you want to write more portable code, you should write GO TO and GO SUB as GOTO and GOSUB, as BASIC Wrangler will fix those for you.
- If you want to see an example of what properly formatted code might look like check out [the Battle System Test I wrote](http://github.com/pahandav/battle-test).

## Converting Programs to BASIC Wrangler

As I haven't written a labeling routine yet, you can use [C64List](https://www.commodoreserver.com/Downloads.asp) to convert programs into BASIC Wrangler format. Note that C64List will turn everything in your program into upper-case, so this is only meant as a temporary solution.
To convert, type:

```Batchfile
C64List <file name> -lbl
```

Then type:

```Batchfile
bw convert <file name>.lbl -c
```

Your file will now be known as `<file name>.lbn`

## DATA Statement Reformatter

This will move all the DATA statements in your program to the end of the listing, and allow BASIC Wrangler to correctly format them for the line length in your desired BASIC dialect.

***Do not use this feature if your program RESTOREs to a particular line number.***

To use, type: (if you add -d to the prior command, it will also convert the data statements)

```Batchfile
bw convert <file name> -d
```

Your file will now be reformatted as `<file name>.dat`

## Some of the Planned Features

- [ ] Built-in conversion from numbered listings routine
- [x] A GUI
- [x] Output to clipboard when pasting
- [ ] Preprocessor macros like includes and ifs
- [ ] Renaming variables
- [ ] Support for external tokenizers by accounting for how many bytes each token uses
- [x] Support for output to files that can be transferred directly into disk images

## Changelog

### 0.02.0 - 2019-10-27

- File mode with more command line arguments
- Paste mode now places output directly onto the clipboard so you can paste directly into emulators
- A basic GUI has been added
- Various minor fixes and refactoring

### 0.01.0 - 2019-10-24

- Initial release
