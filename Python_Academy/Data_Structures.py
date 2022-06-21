fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana',4)) #find next banana starting at position 4
print(fruits.reverse())
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())

#Methods such as insert, remove, and sort return the default of "None" which is the design principle for all mutable data structures in Python

#Not all data can be sorted. For example, integers can't be compared to strings and "None" can't be compared to other types

#Using lists as stacks:

stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

#Can also use lists as queues, and follows FILO (first in, last out). In order to make a queue, use collections.deque
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") #Terry arrives
queue.append("Graham") #Graham arrives
queue.popleft() #First to arrive now leaves
queue.popleft() #Second to arrive leaves
print(queue) #remaining queue in order of arrival

#List comprehensions:

squares = []
for x in range(10):
	squares.append(x**2)

print(squares)

#Can calulcate the list of squares without any side effects using:

squares = list(map(lambda x: x**2, range(10)))

#or

squares = [x**2 for x in range(10)]

#Comprhensions consist of brackets containing an expression followed by a "for" clause, and then 0 or more "for" or "if" clauses. The result is a new list resulting from an evaluation of the expression in the context of the "for" and "if" clauses that follow it. i.e.

print( [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!=y]) #Combines the lists if they are not equal.

print("This is equivalent to") 

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
	if x != y:
	    combs.append((x, y))
print(combs)

#A tuple is used to store multiple items in a single variable

print("If an expression is a tuple i.e. (x,y) it must be parenthesized")

vec = [-4, -2, 0, 2, 4]
#Create a new list with values doubled
print([x*2 for x in vec])
#filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
#Apply function to all elements
print([abs(x) for x in vec])
#call method on each element
freshfruit = [' banana',' loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])
#Create list of 2-tuples like (number, square)
print([x, x**2 for x in range(6)])
#Tuple must be parenthesized, otherwise error is raised
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

#List comprehensions can contain complex expressions and nested functions

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

#Nested List Comprehensions

print("Example matrix")
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print("List comprehensions then becomes:")
print([[row[i] for row in matrix] for i in range(4)])

print("In the real world, want to use built-in functions over complex flow statements")

#The "del" statement

print("The del statement deletes an item in a given index. Unlike pop(), it does not return any value.")

a = [-1,1,66.25, 333, 333, 1234.5]
print(a)
print(del a[0])
print(del a[2:4])
print(del a[:])

#Or delete the entire variable via:
del a

#Tuple example:

t = 12345, 54321, 'hello!'
print(t[0])
print(t)
#Tuples can be nested
u = t, (1,2,3,4,5)
print(u)
#Tuples are immutable but can contain multiple objects
v = ([1,2,3], [3,2,1])
print(v)

#Output tuples are always enclosed in parentheses so that nested tuples are interpreted correctly.
#Tuples are immutable

#Tuples may also contain nothing, as outlined below:
empty = ()
singleton = 'hello', #Notice the trailing comma
print(len(empty))
print(len(singleton))
print(singleton)
#Statement t = 12345, 54321, 'hello!' is an example of tuple packing. The statement can also be reversed:
x, y, z = t
#This is called sequence unpacking


#Sets
print("Sets are unordered collections with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Sets also support operations like union, intersection, difference, and symmetric difference")
basket = {'apple', 'orange', 'pear', 'orange', 'banana'}
print(basket) #Duplicates have been removed
'orange' in basket #Fast membership testing
'crabgrass' in basket

#Demonstrate set operations on unique letters from two words
a = set('willywigger')
b = set('killthat')
print(a) #Unique letters in a
print(a - b) #Letters in a but not in b
print(a | b) #Letters in a, b, or both
print(a & b) #Letters in a & b
print a ^ b) #Letters in a or b but not both
#Set comprehensions are also available:
a = {x for x in 'willywigger' if x not in 'wni'}
print(a)

#Dictionaries

tel = {'jack': 4098, 'sape' : 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
'guido' in tel
'jack' not in tel

#"dict()' constructor also builds dictionaries directly from sequences of key-pair value pairs:

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

#Looping techniques

#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)

#When looping through a sequence, the position of the index and corresponding value can be retrieved at the ame time using the enumerate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#To loop over two or more sequences at the same time:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers): 
    print('What is your favorite {0}? It is {1}.'.format(q,a))

#To loop over a sequence in reverse:
for i in reversed(range(1,10,2)):
    print(i)

#To loop over a sequence in sorted order:
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(f)

#Instead of altering a list while looping over it, safer and recommended to create a new list instead:
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
	filtered_data.append(value)
print(filtered_data)

