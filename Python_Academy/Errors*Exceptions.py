#The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).
#Exception handling is not typically handled by programs, but there are some instances where it is. For example, the KeyboardInterrupt exception which is caused by the user hitting ctrl-c or the equivalent. 

The try statement works as follows.

    First, the try clause (the statement(s) between the try and except keywords) is executed.

    If no exception occurs, the except clause is skipped and execution of the try statement is finished.

    If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

    If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple



class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

#This will print "BCD in that order

#The "raise" statement allows a forced specified exception to occur

#There are "cleanup actions" which are used via "finally" - this is a chunk of code that will execute under all circumstances, whether or not the try raises anything



    If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

    An exception could occur during execution of an except or else clause. Again, the exception is re-raised after the finally clause has been executed.

    If the finally clause executes a break, continue or return statement, exceptions are not re-raised.

    If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution.

    If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.



