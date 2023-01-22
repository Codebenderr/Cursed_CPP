# Cursed C++
Ever wanted to write C++ with pythonic syntax?

## Motivation
I was bored, had nothing better to do and let's admit it, Python's indentation is awesome.
```python
'motivation' is None
```

## Usage

### As a module

You can use this like a regular python module, e.g.

```python
import cursed_cpp

uncursed_code = cursed_cpp.uncurse('code goes here')
```

### As a standalone application


#### Without arguments
If you run the code as a script without any arguments, the content of the clipboard will be uncursed and set as the new clipboard content.
Note that this requires the python library `clipboard` to be installed.

#### With a single filename argument
When a single filename argument is specified, the program will uncurse that file's content and put it in a new file in the same directory named `uncursed_filename.cpp`.

#### With 2 filename arguments
When 2 filename arguments are specified, the program will uncurse the content of the file in the first filename argument, then put it in a new file in the same directory named as the second filename argument.



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
can be rewritten as:
```cpp
#include <iostream>
using namespace std

int main()
  
    int x = 0
  
    for (int i = 0; i < n; i++)
        x += 1
  
    return 0
```
Notice how there is no `:` at the end of the for loop unlike Python, this is because I see them as redundant.

Additionally, the parentheses in `if`, `else if`, `for` and `while` statements can be omitted if desired.
So the above code can further be reduced to:
```cpp
#include <iostream>
using namespace std

int main()
  
    int x = 0
  
    for int i = 0; i < n; i++
        x += 1
  
    return 0
```
However, this is not recommended as it usually makes code less readable, but there's the option to leave the first parenthesis and omit only the second parenthesis, which makes the code a bit more readable:
```cpp
#include <iostream>
using namespace std

int main()
  
    int x = 0
  
    for (int i = 0; i < n; i++
        x += 1
  
    return 0
```
