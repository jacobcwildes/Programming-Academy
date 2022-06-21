#In order to use formatted string literals (to exercise more control over string output, do this:
year = 2022
event = "Referendum"
print(f'Results of the {year} {event}')

#There is also str.format() which requires more manual effort - need to provide the information to be formatted, like so:
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes {2.2%}'.format(yes_votes, percentage)

#Can also make whatever pattern desired using string slicing/concatenation

#When there isn't a need for a fancy output, can convert any value to a string via repr() or str(). str() returns a representation that is more human friendly to read. repr() generates representations that the interpreter can understand, or force a SyntaxError if there is none. If there is no human-friendly representation, str() returns the same as repr()

#example of repr:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

#Formatted string literals: include the value of Python expressions in a string 

import math
print(f'The value of pi is approximately {math.pi:.3f}.') #Passing an interger after the ':' will cause the field to be a minimum number of characters wide, which is handy for making columns line up

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

#Other modifiers can be used to convert value before formatting. "!a" applies ascii(), "!s" applies str(), and '!r' applies repr()

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

#String format method:

#Basic use of the str.format() method looks like this:
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

#Manual string formatting

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    #Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

#The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string. If the input string is too long, they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually better than the alternative, which would be lying about a value. (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)

#Another method is str.zfill() which pads a numeric string on the left with zeros. It also understands + and - signs

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

#Old string formatting
#The % operator (modulo) can be used for string formatting. Given 'string % values' instances of % in string are replaced with zero or more elements of 'values' Commonly known as string interpolation

import math
print('The value of pi is approximately %5.3f.' % math.pi)

#Reading and writing files

#open() returns a file object and is most commonly used with two positional arguments and one keyword argument. i.e. open(filename, mode, encoding=None)

f = open('workfile', 'w', encoding = "utf-8")

#The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

#In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.

#good practice to use the "with" keywrod when dealing with file objects. This ensures that the file fully closes, whether or not an exception was ever raised.

with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

#can check and see if the file has fully closed:
f.closed

#Methods of file objects:

#Assuming that there is a file already written named f:

#Use f.read() is useful for going through an entire file. Be cautious that the file is not larger than the system memory.
#f.readline() reads from a single line in the file. Once the end of the file has been reached, the method returns a blank line like so: ' '

#Can also loop over a file like so:

for line in f:
    print(line, end=' ')

#There is also f.write(string) which write the contents of "string" to the file, returning the number of characters written. 
f.write('this is a test\n') #which returns 15 in this case

#f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

#To change the file object’s position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the whence argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

#If you have an object, x, can view its JSON string representation with a simple code:

import json

x = [1, 'simple', 'list']
json.dumps(x)

#JSON files MUST be encoded in UTF-8


