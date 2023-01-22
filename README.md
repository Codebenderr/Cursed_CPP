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
You can specify a filename argument which the program will read and then make a new file in the same directory called `cursed_filename.cpp`.

#### Without arguments
If you run the code as a script without any arguments, the content of the clipboard will be pythonified and set as the new clipboard content.
Note that this requires the python library `clipboard` to be installed.


## What It Does
You can omit the curly braces and semicolons in C++ and instead use indentation similar to Python, e.g.

```cpp
#include <iostream>
using namespace std;

int main()
{
  
    int x = 0;
  
    for (int i = 0; i < n; i++)
    {
        x += 1;
    }
  
    return 0;
}
```
can be rewritten as
```cpp
#include <iostream>
using namespace std

int main()
  
    int x = 0
  
    for (int i = 0; i < n; i++)
        x += 1
  
    return 0
```
Notice how there is no `:` at the end of the for loop unlike in Python, this is because I see them as redundant.

Additionally, the parentheses in `if`, `else if`, `for` and `while` statements can be omitted if desired.
So the above code can further be reduced to
```cpp
#include <iostream>
using namespace std

int main()
  
    int x = 0
  
    for int i = 0; i < n; i++
        x += 1
  
    return 0
```
