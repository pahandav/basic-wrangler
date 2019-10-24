# basic-wrangler

A BASIC program listing line renumberer/cruncher.

***This program is currently in alpha testing.*** It will probably break your program. The documentation is minimal. Things will change frequently.

## Purpose

The purpose of BASIC Wrangler is to allow you to write BASIC programs using labels in a dialect-agnostic way. It also combines and crunches lines to take up the least amount of space, thus saving you memory. It is designed to be able to work with almost any dialect of line numbered BASIC.

## Requirements

- Python 3 (any version of 3 should work, only tested with 3.7)

## Usage

```Batchfile
bw <BASIC Type> <filename>
```

The BASIC Type is the dialect of BASIC that you wish to use. You can find all the current definitions in [`basdefs.py`](basdefs.py). When in doubt, specify bascom, as it's the closest thing to a generic version. It will typically output to `<filename-out>.bas`. You can then open the file and paste the code into an emulator.

## Special Notes

The Commodore Amiga dialect is set up to use the ACE BASIC Compiler. Copy the .b file to a shared emulator directory, and run `bas -iO <filename minus the .b>` to compile it.

The RISC OS dialect needs to be tokenized to be runnable. To do this, copy the ,ffb file to a shared emulator directory, load it in RISC OS by shift-double-clicking it, and then save it back with F3.

The ZX81 and ZX Spectrum dialects are meant to be tokenized by the EightyOne emulator, but other tokenizers should be able to handle the output files.

## Writing Programs for BASIC Wrangler

- *Write one statement per line* unless you're doing something complicated with IF statements. A statement is whatever you would write up until you hit a colon to seperate statements.
- *Write with spaces where appropriate*. BASIC Wrangler will deal with the output spacing for you.
- You should write all BASIC keywords in **upper-case**.
- Labels **MUST** start with a ` (backtick, the key the tilde is on) character. Hopefully, that won't collide with any keywords from any BASIC dialect.
- To indicate a jump target, you should have the label on its own on the line directly preceding the jump target. You can add a colon after the jump target label if you wish.
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
fix-output <file name>.lbl
```

Your file will now be known as `<file name>.lbn`

## DATA Statement Reformatter

***This feature is currently kind of buggy, and so it may or may not work for you.***

This will move all the DATA statements in your program to the end of the listing, and allow BASIC Wrangler to correctly format them for the line length in your desired BASIC dialect.

***Do not use this feature if your program RESTOREs to a particular line number.***

To use, type:

```Batchfile
data-format <file name>
```

Your file will now be reformatted as `<file name>.dat`

## Some of the Planned Features

- [ ] Built-in conversion from numbered listings routine
- [ ] A GUI
- [ ] Output to clipboard when pasting
- [ ] Preprocessor macros like includes and ifs
- [ ] Renaming variables
- [ ] Support for external tokenizers by accounting for how many bytes each token uses
- [ ] Support for output to files that can be transferred directly into disk images

## Changelog

### 0.01.0 - 2019-10-24

- Initial release
