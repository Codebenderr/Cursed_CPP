# Cursed C++
Ever wanted to write C++ with pythonic syntax? Now you can!

## Motivation
I was bored, had nothing better to do and let's admit it, Python's indentation is awesome.

## Usage

### As a module

You can use this like a regular python module, e.g.

```python
import cursed_cpp

pythonified_code = cursed_cpp.pythonify('code goes here')
```

### As a standalone application

#### With a filename argument
You can specify a filename argument which the program will read and then make a new file in the same directory called cursed_filename.cpp

#### Without arguments
If you run the code as a script without any arguments, the contents of the clipboard will be pythonified and set as the new clipboard contents
Note that this requires the python library `clipboard` to be installed
