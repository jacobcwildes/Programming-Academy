#A module is a file containing Python definitions and statements
#for example: Fibonacci numbers module
def fib(n): #Write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(n): #Return Fibonacci series up to n
    result = []
    a, b = 0,1
    while a < n:
	result.append(a)
	a, b = b, a+b
    return result

#Then enter a python interpreter and import the module via:

#import <filename>

#This does not enter the names of the functions defined in the file directly into the symbol table. It only enters the module name. From there you can access the function. i.e.
#fibo.fib(1000)
#fibo.fib2(100)
#fio.__name__
#If going to use a function a lot, assign it a local name:
#fib = fibo.fib
#fib(500)


#It is good form to do all imports at the beginning of a file

#for example:

#from fibo import fib, fib2

#fib(500)

#This does NOT introduce the module name from which the imports are taken in the local sykbol table

#If you want to import ALL the names that a module defines:

#from fibo import *

#This imports all names except those preceded by an underscore(_)
#This is bad practice in a finished product

#The built in "dir()" function is used to find out which names a module defines. It returns a sorted list of strings.
#Without arguments, "dir()" returns the list of names you have defined currently

#dir() does not list the names of built-in functions and variables. To list them, use builtins like so:
#import builtins
#dir(builtins)

#Packages:

#Packages have a name scheme that is as follows: A.B. Which means there is a submodule, B, in a package named A.

#When importing packages, Python searches through the directories on sys.path looking for the package subdirectory

#__init__.py files are requited to make Python treat directories containing the file as packages. This prevetns directories with a common name (i.e. string) from unintentionally hiding valid modules that occur later on the module search path. At its simplest, the __init__.py can just be an empty file.


