# logging module builtin
    # simple print statement used for debugging on fly but logging better

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)

sub_result = subtract(num_1, num_2)

mul_result = multiply(num_1, num_2)

div_result = divide(num_1, num_2)

# can use simple print statements to check results
    # now using logging

#----------------------------------------------------------------------------- 

import logging

# logging levels 
    # DEBUG: Detailed information, typically of interest only when diagnosing problems.

    # INFO: Confirmation that things are working as expected.

    # WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

    # ERROR: Due to a more serious problem, the software has not been able to perform some function.

    # CRITICAL: A serious error, indicating that the program itself may be unable to continue running.


# by default logging level set to WARNING and above they are logged automatically and whereas DEBUG and INFO are ignored

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
    # default behaviour of logging statements is just to log these to the console 
    # similar to print statement but since default logging level is WARNING and higher DEBUG and INFO not logged to console

logging.warning('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
    # OP >> WARNING:root:Mul: 20 * 10 = 200
        # warning logging level 
logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))

#----------------------------------------------------------------------------- 
# can explicitly set logging level above use basicConfig() method on logging
import logging
logging.basicConfig(level=logging.DEBUG)
# .....code ....
                # .debug() and .DEBUG are different .DEBUG is a constant that an integer in background
                    # generally these integers are increment of 10
                        # DEBUG 10
                        # INFO 20
                        # WARNING 30 and so on ... 


#----------------------------------------------------------------------------- 
# to log to file instead of console to remember state of errors set fileName in basicConfig()
logging.basicConfig(filename='52_LogFile.log',level=logging.DEBUG)
    # if varaibles changed and program rerun then Log is appended to log file not over written
    # file created if not exists

#----------------------------------------------------------------------------- 
# by default format of log file
    # WARNING:root:{Program values print - Mul: 20 * 10 = 200}
    # change format explicitly in basicConfig()

# https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(filename='52_LogFile.log',level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(message)s')
    # refer format attributes in docs link above

#-----------------------------------------------------------------------------
    # using logging in practical example  
# employee.py

import logging

logging.basicConfig(filename='52_LogFile.log',level=logging.INFO,
format='%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')