# `Python: Basic Function Calls`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:

1. [`Common Built-in Functions for Beginners`](#common-built-in-functions-for-beginners)
1. [`Quickstart Guide to Functions`](#quickstart-guide-to-functions)
1. [`The print() Function Call`](#the-print-function-call)
    1. [`print() multiple comma seperated values`](#print-multiple-comma-seperated-values)
    1. [`end parameter`](#end-parameter)
    1. [`sep parameter`](#sep-parameter)
    1. [`file parameter`](#file-parameter)
    1. [`flush parameter`](#flush-parameter)
1. [`The input() Function Call`](#the-input-function-call)
    1. [`prompt parameter`](#prompt-parameter)
1. [`The len() Function Call`](#the-len-function-call)
1. [`The type() Function Call`](#the-type-function-call)
1. [`Nested Function Calls`](#nested-function-calls)

# `Common Built-in Functions for Beginners`
* `print(*values, sep=" ", end="\n", file=None, flush=False)`
* `input(prompt="")`
* `int(), float(), complex()`
* `len(obj)`

* `type()`

<br>

[Back to Top](#python-basic-function-calls)

___

<br>

# `Quickstart Guide to Functions`
|Term| |Definition|
|:-:|:-|:-|
|Function Definition|explains how to perform a task| block of code that specifies a sequence of statements to perform a specific task.<br> It includes the function's name, parameters (if any), and the body of the function which contains the executable code.|
|Function Call|executes the function and returns result| the process of invoking or executing a function that has been defined earlier.|
|Parameters|optional variables| variables inside the parenthesis that are used to pass information into functions or methods|
|Arguments|depends on the number of parameters| the actual values or data you pass to a function's parameters when you call the function|
|Return| optional| returns the result of a function to the caller(Function Call)|

<br>

General Function Definition Syntax:

    def function_name(parameter1, parameter2, ...):
        ...

*The 'Built-in Function Calls we will use here are defined for us by the Python Standard Library*

General Function Call Syntax:

    function_name(argument1, argument2, ...)

<br> 

## Function Definition and Call Example:

```python
# Function Definition
def add(a, b):
    return a + b

#Function Calls
add(2,2)    # Returns: 4
add(5,4)    # Returns: 9
add(2,10)   # Returns: 12


#Function Call and store the result in a variable
a = add(2,2)    # a = 4
b = add(5,4)    # b = 9
c = add(2,10)   # c = 12

#Function Call and print() output
print(add(2,2))    # Outputs: 4
print(add(5,4))    # Outputs: 9
print(add(2,10))   # Outputs: 12
```

<br>

[Back to Top](#python-basic-function-calls)

___

<br>

# `The print() Function Call`
The `print()` function call is used to send data to the standard output (std.out) or to a file


`Standard output (stdout)` refers to the default destination for output generated by a program during its execution. 
> In many operating systems and programming environments, standard output is typically associated with the display, monitor, or console where the program's output is visible to the user.

<br>

syntax:

    print(*values, sep=" ", end="\n", file=None, flush=False) 


> * each of the variables inside the parenthesis are called parameters
> * parameters with an = and a value are optional parameters meaning they can be provided an argument, but it is not required. The value is the default value for that parameter

<br>

## Basic print() Call Examples


```python
print()                   # Output: 
print(True)               # Output:  True
print(10)                 # Output:  10
print(2.17)               # Output:  2.17
print(5j)                 # Output:  5j
print("Hello World")      # Output:  Hello Worldwd
print(["a","b","c"])      # Output:  [a,b,c]
print(("a","b","c"))      # Output:  (a,b,c)
print({"a","b","c"})      # Output:  {a,b,c} 
print({"a":97,"b":98})    # Output:  {a:97,b:98}
```
<br>

## `print() multiple comma seperated values`
* by default each value will be seperated by a space 


```python
print("one", "two", "three", "four")
# Output: one two three four
```
<br>

## `end parameter`
> * the `print()` call has a built-in parameter called 'end'
> * by default the value of 'end' is "\n" (a newline character)
> * when `print()` is called, after printing the cursor goes to a new line
> * 'end' is a keyword parameter (must be set using its name)


```python
print("Hello")
print("World")
# Output:
# Hello
# World
```

* use ,end = "" to keep the cursor on the same line


```python
print("Hello", end = "") #default is "\n" a newline character
print("World")
# Output: HelloWorld
```
<br>

## `sep parameter`
> * the `print()` function call has a built-in parameter called 'sep'
> * 'sep' specifies a separator between each comma separated value. 
> * the default value of 'sep' is " " (a space character)
> * 'sep' is a keyword parameter (must be set using its name)


```python
print("Hello", "World") # Output: Hello World
```

* use ,sep = "" to specify a new separator 


```python
print("Hello", "World", sep = "|") # Output: Hello|World
print("Hello", "World", sep = "-") # Output: Hello-World
print("Hello", "World", sep = ":") # Output: Hello:World
print("Hello", "World", sep = "_") # Output: Hello_World
print("Hello", "World", sep = " ") # Output: Hello World
print("Hello", "World", sep = "*") # Output: Hello*World
print("Hello", "World", sep = "=") # Output: Hello=World
print("Hello", "World", sep = "~") # Output: Hello~World
```
<br>

## `file parameter`
> * the `print()` funciton call has a built-in parameter called 'file'
> * 'file' specifies a file where to write the output
> * the default value of 'file' is the Standard Output (stdout)
> * 'file' is a keyword parameter (must be set using its name)


```python
print("Hello World") # Output: Hello World
```

* use ,file = "" to specify a file path to which to write the output


```python
print("Hello World", file = "output.txt") # Writes to output.txt: Hello World
```
<br>

## `flush parameter`
> * the `print()` function call has a built-in parameter called `flush`
> * `flush` specifies if the output buffer will be flushed after printing
>     * determines whether or not output is buffered or immediately output
> * the default value of `flush` is False
> * `flush` is a keyword parameter (must be set using its name)


* use , `flush =`  to set the value of flush

```python
print("Hello World", flush = True) #Output: Hello World
```

*This can be useful in situations where you want to see the output in real-time, especially when monitoring progress or debugging.*


```python
import time # importing code from the standard library
for num in range(5):
    print(num)
    time.sleep(1) # wait 1 second

#Output: 
# 0
# 1
# 2
# 3
# 4

# Here the output all occurs at once due to buffering
```


```python
import time # importing code from the standard library

for num in range(5):
    print(num, flush = True)
    time.sleep(1) # wait 1 second

#Output: 
# 0
# 1
# 2
# 3
# 4

# Here the output all occurs in real time, with no buffering
```

*The output buffer refers to a temporary storage area where the data to be printed by the `print()` function is held before it's actually displayed.*

When you call `print()`, Python doesn't immediately write the output to the console or file.    
Instead, it stores the output in this buffer until certain conditions are met.  

<br>

[Back to Top](#python-basic-function-calls)

___

<br>

# `The input() Function Call`

`input()` pauses the execution of the program and reads in user input data from standard input (std.in)**

Standard input:
> (often abbreviated as stdin) refers to the default source of input data for a program. It is a stream from which a program reads its input data.*

syntax:

    input(prompt="")

> * `input()` always returns a  string `<class 'str'>` type
> * `input()` reads from Standard Input (stdin)
> * If prompt is not given an argument, the default is an empty string "" 


```python
input() # the program will stop here and wait for the user to type in a value
```
<br>

## `prompt parameter`
> * the `input()` function call has a built-in parameter called 'prompt'
> * 'prompt' specifies what to print out before accepting user input
> * the default value of 'prompt' is "" (an empty string)
> * 'prompt' can be assigned by position or keyword


```python
input() # prompt with default value ""

input("Type your input: ") #prompt assigned by position

input(prompt = "Type your input: ") #prompt assigned by keyword

```
<br>

## `Storing User Input`
> * the user input returned from a call to `input()` can be stored using a variable, and used later



```python
user_input = input("Please input a value: ")
print(user_input)
```

a program can ask for multiple inputs with multiples calls to `input()`


```python
first_name = input("First name: ")
last_name = input("Last name: ")

print(first_name, last_name)
```

<br>

## `Numbers as User Input`
> * `input()` by default returns a string `<class 'str'>`
>   * strings `<class 'str'>` cannot do math

> * strings can be converted into integers `<class 'int'>` with the int() constructor


```python
int(input("Write a whole number: "))

# Math example
x = int(input())
y = int(input())

print(x + y) # Outputs the sum of x and y
```

* strings can be converted into floats `<class 'float'>` with the float() constructor


```python
float(input("Write a fractional number: "))

# Math example
x = float(input())
y = float(input())

print(x + y) # Outputs the sum of x and y
```

* strings can be converted into complex numbers `<class 'complex'>` with the complex() constructor


```python
complex(float(input("Write the real part: ")), float(input("Write the imaginary part (omit j): ")))

#it is necessary to ask for the whole and imaginary parts separately

# Math example
x = complex(float(input("Real Part: ")), float(input("Imaginary Part" )))
y = complex(float(input("Real Part: ")), float(input("Imaginary Part" )))

print(x + y) # Outputs the sum of x and y
```

<br>

[Back to Top](#python-basic-function-calls)

___

<br>

# `The len() Function Call`
`len(object)` function call returns the number of items (length) in an object.

syntax:
```
len(object)
```
example:
```python
len("hello")  # Returns 5, because the string "hello" has 5 characters
```
```python
word = "Python"
len(word)  # Returns 6

```
```python
fruits = ["apple", "banana", "cherry"]
len(fruits)  # Returns 3

mixed_list = [1, "apple", 3.14, True]
len(mixed_list)  # Returns 4

```
```python
coordinates = (10, 20, 30)
len(coordinates)  # Returns 3
```
> When used on dictionaries `len()` counts the number of key-value pairs, not individual keys or values
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
len(person)  # Returns 3s
```
> When used on nested structures `len()` will only count the top-level items
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
len(nested_list)  # Returns 3, because there are three sublists
```

<br>

[Back to Top](#python-basic-function-calls)

___

<br>

# `The type() Function Call`
The `type()` function returns the type of an object. It is often used to check the data type of a variable or value.

syntax:
```
type(object)
```
```python
type(None)                   # Returns: <class 'NoneType'>
type(True)                   # Returns: <class 'bool'>
type(5)                      # Returns: <class 'int'>
type(3.14)                   # Returns: <class 'float'>
type(1j)                     # Returns: <class 'complex'>
type("a")                    # Returns: <class 'str'>
type("Hello")                # Returns: <class 'str'>
type(["a","b","c"])          # Returns: <class 'list'>
type(("a","b","c"))          # Returns: <class 'tuple'>
type({"a","b","c"})          # Returns: <class 'set'>
type({"a":97,"b":98,"c":99}) # Returns: <class 'dict'>
type(len)                    # Returns: <class 'builtin_function_or_method'>
```

<br>

[Back to Top](#python-basic-function-calls)

___

<br>

# `Nesting Function Calls`

Nesting is the placing of one construct inside of another
> * Collections, Conditionals, Loops, Functions, Methods, Classes, etc. can be nested in Python

examples:

## `Nested Lists`


```python
[[],[],[],[],[]] #List of empty lists

[[1,2,3],[4,5,6],[7,8,9]]

[['apple', 'banana', 'orange'], ['grape', 'kiwi', 'melon'], ['pear', 'plum', 'peach']]

[[10, 20, 30], [40, 50, 60], [70, 80, 90]]

[['John', 25, 'male'], ['Jane', 30, 'female'], ['Alex', 35, 'male']]

[[True, False, True], [False, True, False], [True, True, False]]

[[(1, 2), (3, 4)], [(5, 6), (7, 8)], [(9, 10), (11, 12)]]

[[{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}], [{'name': 'Alex', 'age': 35}, {'name': 'Emma', 'age': 40}]]

```

## `Nested Conditionals`


```python
if():
    if():
        if():
            ...
```

## `Nested While Loops`


```python
while():
    while():
        while():
            ...
```

## `Nested For Loops`


```python
for _ in range():
    for _ in range():
        for _ in range():
            ...
```

## `Nested Function Calls`


```python
print(int(input("Type your input:\n")))
#The input function is inside of the int function which is inside of the print function.
```


```python
#This is just used to illustrate how nesting works, it is not syntatically correct Python
          input("Type your input:\n") #This is executed first, and its result returned
      int(                           ) #This is executed second, uses the result returned from input() as an argument, and its result is returned
print(                                ) #This is executed last, and uses the result returned from int()
```

<br>

___

[Back to Top](#python-basic-function-calls)

___

<br>

*Created and maintained by Mr. Merritt* 
