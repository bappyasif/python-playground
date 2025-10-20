# introduction to exceptions

we are probably very familiar with the most common type of error: a syntax error. Syntax errors are mistakes in the structure of Python code

As opposed to a syntax error, an exception is a different kind of error that can occur with syntactically correct code

Exceptions are runtime errors because they occur during program execution, only when the offending code (the code causing the error) is reached

An example of an exception, and one we have probably seen before, is a NameError

Although the NameError has a similar output to a SyntaxError (both end with Error)

Exceptions and syntax errors make up the two core categories for any error we will run into

python errors can be divided into syntax errors, exceptions

A traceback is a summary that includes the exception type, a message, and the series of function calls preceding the exception, along with file names and line numbers


# builtin exceptions

exceptions are objects just like anything else, most exceptions inherit deirectly from a class called `exception`, however they all are direvided directly or otherwise from `BaseException` class

```python
print(NameError.__bases__)
```
will output <class 'Exception'>

we can even call __bases__ on exception class to see is origin
print(Exception.__bases__) will output <class 'BaseException'>

full heirarchy of built in exceptions:
BaseException
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError

Note that there are a lot of exceptions built into the language of Python, and we dont need to memorize all of them.

```python
sale_instruments = ['Violin', 'Conga', 'Clavinet']

print('The following ' + len(sale_instruments) + ' instruments are on sale:') # 
print(sale_instruments[0])
print(sale_instruments[1])
print(sale_instruments[3])
```