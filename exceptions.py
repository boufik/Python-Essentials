# 0. A simple example
while True:
    try:
        x = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")



# 1. Class 'Exception' methods
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))       # the exception type
    print(inst.args)        # arguments stored in .args
    print(inst.__str__())   # __str__ allows args to be printed directly, but may be overridden in exception subclasses
    x, y = inst.args
    print('x =', x)
    print('y =', y)



# 2. Multiple Exceptions
import sys

try:
    f = open('testfile.txt')                  # Chance for OSError Exception if there is no such file or directory
    s = f.readline()
    i = int(s.strip())                        # Chance for ValueError Exception if s can not be converted into an integer
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise



# 3. Force an Exception to happen
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise



# 4. 'Else' is activated along with 'try', while 'finally' is activated with both 'try' and 'except'
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Try clause execution has failed. Division by zero!")
    else:
        print("Else clause is being executed after successful execution of try clause. The result is", result)
    finally:
        print("Finally clause is being executed")

divide(2, 1)
divide(2, 0)



# 5. Raising and Handling Multiple Unrelated Exceptions
def f():
    excs = [OSError('Error 1'), SystemError('Error 2')]
    raise ExceptionGroup('There were problems', excs)


try:
    f()
except Exception as e:
    print(f"Exception caught: {type(e)}: {e}")
