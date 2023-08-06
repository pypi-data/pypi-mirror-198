# VBA-like Functions in Python

This module provides a set of VBA-like functions that you can use directly in your Python projects. Save the `cC.py` file to your project folder and import the functions using the following import statement:

```python
from cC import *
```

Alternatively you can import it with `pip`.

```python
pip install -U morvba
```
---
# Functions

## savesetting(a='', b='', c='', d='')
Save a setting to an INI file.

**Arguments:**

- `a`: Group name
- `b`: Subgroup name
- `c`: Item name
- `d`: Value

**Example:**

```python
savesetting("app", "window", "width", "1024")
```

---
## getsetting(a='', b='', c='', d='')
Retrieve a setting from an INI file.

**Arguments:**

- `a`: Group name
- `b`: Subgroup name
- `c`: Item name
- `d`: Default value (optional)

**Example:**

```python
window_width = getsetting("app", "window", "width", "")
```

---
## left(str_text='', int_len=1)
Return the left part of a string.

**Arguments:**

- `str_text`: Input string
- `int_len`: Number of characters to return (default is 1)

**Example:**

```python
result = left("Hello, world!", 5)
```

---
## right(str_text='', int_len=1)
Return the right part of a string.

**Arguments:**

- `str_text`: Input string
- `int_len`: Number of characters to return (default is 1)

**Example:**

```python
result = right("Hello, world!", 6)
```

---
## mid(str_text='', int_start=1, int_len=1)
Return a substring from the middle of a string.

**Arguments:**

- `str_text`: Input string
- `int_start`: Starting position
- `int_len`: Number of characters to return

**Example:**

```python
result = mid("Hello, world!", 8, 5)
```

---
## pricap(str_text='')
Capitalize the first letter of each word in a string.

**Arguments:**

- `str_text`: Input string

**Example:**

```python
result = pricap("hello, world!")
```

---
## instr(int_start=1, str_text='', str_what='')
Return the position of a substring in a string.

**Arguments:**

- `int_start`: Starting position
- `str_text`: Input string
- `str_what`: Substring to search for

**Example:**

```python
position = instr(1, "Hello, world!", "world")
```

---
## trim(str_text='', str_char=' ')
Trim spaces or a specific character from a string.

**Arguments:**

- `str_text`: Input string
- `str_char`: Character to trim (default is space)

**Example:**

```python
result = trim("   Hello, world!   ")
```

---
## pkey(str_text='', str_ini='', str_end='', boo_trim=True)
Extract a string between two delimiters.

**Arguments:**

- `str_text`: Input string
- `str_ini`: Starting delimiter
- `str_end`: Ending delimiter
- `boo_trim`: Whether to trim spaces (default is True)

**Example:**

```python
result = pkey("Example: [Hello, world!]", "[", "]")
```
---
You can use these functions in your Python code without referencing the class name, just like you would in VBA.
