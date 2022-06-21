print(2+2)
print("-----------------------")
print(50 - 5*6)
print("-----------------------")
print(8/5) #division will always return a floating point number
print("-----------------------")
print((50 - 5*6)/4)
print("-----------------------")

print("\n")

print("17/3")
print(17//3) #Floor division discards the fractional portion
print(17%3) #% Operator returns division remainder
print(5*3+2) #floored quotient * divisor + remainder

#Can use "**" to calculate powers
print(5**2)
print(2**7)

#Equals sign is used to assign value to a variable. After doing this, no value is displayed at the next prompt. i.e.
width = 20
height = 5*9
#in order for this to appear, must say "print" like so:
print(width*height)

#if a variable is not assigned, the program will throw an error.

#Python can also interact with strings, and single or double quotes can be used. Each has the same effect

#single quote example:
print('spam eggs')

#use \' to escape single quote:
print('doesn\'t')

#or use double quotes instead:
print("doesn't")

print('"Yes," they said.')

#or

print("\"Yes,\" they said")

#or

print('"Isn\'t", they said')

#In order to prevent misinterpretation of special characters such as this:
print('C:\some\name') #which will interpret the '\n' and make a new line
#do this:
print(r'C:\some\name')

#String literals can span multiple lines. One way is to use triple-quotes like so:
print("""\
Usage: thingy [OPTIONS]
    -h                  Display this usage message
    -H hostname         Hostname to connect to
    """)

#Strings can be concatenated with the '+' operator and repeated with '*'. i.e.
print(3*'un'+'ium')

#two or more strings literals (between qutoes) next to each other are automatically concatenated
print('Py' 'thon')

#cannot concatenate a variable and a string literal

#strings can be indexed with the first character having an index of 0.

word = 'Python'

print(word[0])
print(word[5])

#strings could also be negative numbers, to start counting from the right:
print(word[-1])
print(word[-2])
print(word[-6])

#negative 0 is the same as positive 0, so negative indices start from -1

#Can also slice strings:
print(word[0:2]) #characters from position 0 (included) to 2 (excluded)
print(word[4:]) #characters from position 4 (included) to the end
print(word[-2:]) #characters from second to last (included) to the end
#Start is ALWAYS included, and the end is ALWAYS included

#Python strings cannot be changed. If in need of a different string, should make a new one:
print('J' + word[1:])
print(word[:2] + 'py')

#Built in 'len' function returns the length of a string

s = 'supercalifraglisticexpialidocious'
print(len(s))

#Python also has lists! i.e.

squares = [1,4,9,16,25]
print(squares)

#Like strings, lists can be indexed and sliced
print(squares[0])
print(squares[-1])
print(squares[-3:])

#Lists also support concatenation
print(squares + [36,49,64,81,100])

#it is possible to change their content!

cubes = [1,8,27,65,125] #the cube of 4 is not 65
print(cubes)
print(4**3, 'blegh, wrong')
cubes[3] = 64 #replace the bad value
print(cubes)

#Can also add new items to the end of the list like so:
cubes.append(216)
cubes.append(7**3)
print(cubes)

#Assignment to slices is also possible, and can change the list or clear it entirely

letters = ['a','b','c','d','e','f','g']
print(letters)
#now replace some of the values:
letters[3:5] = ['C','D','E']
print(letters)
#Now remove the letters
letters[2:5] = []
print(letters)
#clear the entire list by replacing all elements with an empty list:
letters[:] = []
print(letters)

#len function also applies to lists:
letters = ['a','b','c','d']
len(letters)

#It is also possible to nest lists together:
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1])

#Some basic programming

#Fibonacci series:
#the sum of two elements defines the next
a,b = 0,1
while a < 10:
    print(a)
    a, b = b, a+b

#CONTROL FLOW STATEMENTS:

#if statements:

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#for statements

#measure some strings:
words = ['cat','window','defenestrate']
for w in words:
    print(w, len(w))
#Some other ways to make new lists/collections
users = {'Hans': 'active', 'Elenore': 'inactive', 'Wobby': 'active'}

print(users)

#Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)
#Strategy: Create a new collection:
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(users)

#range function i.e.:
for i in range(5):
    print(i)

#It is possible to have the range start from a particular number

print(list(range(5,10)))
print(list(range(0,10,3)))
print(list(range(-10,-100,-30)))

#To iterate over indices of a sequence, can combine range() and len():
a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])
#If you only print the range like so it will return "range(0,10)"

#Can also do arithmetic with like so:
print(sum(range(4))) #0+1+2+3

#Break statements break out of the innermost enclosing "for" or "while" loop i.e.
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        #loop fell through without finding a factor
        print(n, 'is a prime number')

#Continue statements:

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


#pass statements:

#good for placeholders for not yet written functions

#match statements:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not alowed"
        case _:
            return "Something's wrong with the internet"

#"_" never fails to match. If that were not included, it is possible that nothing would match and the branches would fail to execute

#can also combine several literals in a single patten using "|" as seen above

#Patterns can look like unpacking assignments and can be used to bind variables
#point is an (x,y) tuple
#match point:
#    case (0,0):
#        print("Origin")
#    case (0,y):
#        print(f"Y={y}")
#    case (x,0):
#        print(f"X={x}")
#    case (x,y):
#        print(f"X={x}, Y={y}")
#    case _:
#        raise ValueError("Not a point")

#Example using classes to structure data, like so:

class Point:
    x: int
    y: int
def where_is(point):
    match point:
        case Point(x=0,y=0):
            print("Origin")
        case Point(x=0,y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
#can also nest pattens together

#match points:
#    case []:
#        print("No points")
#    case [Point(0, 0)]:
#        print("The origin")
#    case [Point(x, y)]:
#        print(f"Single point {x}, {y}")
#    case [Point(0, y1), Point(0, y2)]:
#        print(f"Two on the Y axis at {y1}, {y2}")
#    case _:
#        print("Something else")
#can also set an "if" clause to the pattern, which will act as a guard. If it is false, the match goes on to the next block
#match point:
#    case Point(x,y) if x == y:
#        print(f"Y=X at {x}")
#    case Point(x,y):
#        print(f"Not on the diagonal")
#subpatterns may be captured using the "as" keyword:
#case (Point(x1, y1), Point(x2, y2) as p2)...

#Most literals are compared by equality, however the singletons "true," "false," and "none"

#Patterns may use named constants which must be dotted names to prevent them from being interpreted as capture variable:

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
color = Color(input("Enter your choice of 'red', blue', or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

def fib(n): #write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

#now call just defined function:
fib(2000)

#keyword "def" introduces a function definition which must be followed by the function name and the parenthesized list of formal parameters

fib

f = fib

print(f(100))

fib(0)
print(fib(0))

#In Python, even functions without return statements still return a value, but nothing special. It returns "None" which is suppressed by the interpreter unless run through a print statement

#To return a list of Fibonacci series:

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        resuslt.append(a)
        a, b = b, a+b
    return result
f100 = fib2(100) #call the function
print(f100) #write the result

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#Function could be called in many ways!
#Give only mandatory argument: ask_ok("Do you really want to quit?")
#Give one of the optional arguments: ask_ok("OK to overwrite the file?", 2)
#or give all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#The "in" keyword tests whether or not a sequence contains a cetain value

i = 5
def f(arg=i):
    print(arg)
i = 6
f()
#will print 5
#NOTE: The default warning is evaluated only once, which makes a difference when the default is an object such as a list, dictionary, or instances of most classes. For example, the argumetns passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
#Functions can be called using keyword arguments
