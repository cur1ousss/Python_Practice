# WARNING:root:Mul: 20 * 10 = 200
    # root means working with default root logger
    # for larger applications better to use specific logger that can be configured separately

# working with root logger not best because -

# when you import module it actually runs the code from that module when its imported 
    # so the configuration of earlier imported module's logger is followed , hence the configuration in current files does'nt work , also since logger level was info in earlier imported module, debug level in current module does'nt log since below {? maybe logs higher check}

import logging
import employeee # its logger configuration for Root logger overrides the logger config below , since both share root logger therefore better to separate and configure loggers for each case separately
    # https://www.youtube.com/watch?v=jxmzY9soFXg

logging.basicConfig(filename='52_LogFile.log',level=logging.INFO,
format='%(levelname)s:%(message)s')
logging.basicConfig(filename='sample.log',level='DEBUG',format='%(asctime)s:%(name)s:%(message)s')
    # can also level='DEBUG' or level=logging.DEBUG

# employee.py
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


#-----------------------------------------------------------------------------

# using Separate loggers

# employee.py
import logging

logger=logging.getLogger(__name__)
        # could hardcode any name in .getLogger(CustomName)
        # but by convetion use __name__ variable , when executed this will be equalt to __main__ and when this code is executed from an import the __name__ will be equal to module's name 
            # https://www.youtube.com/watch?v=sugvnHA7ElY
                # __name__== __main__ 
                    # refer 56. name main .py
                    # when module executed directly name will be equals to main
                    # when this code is executed from an import its name will be equal to the modules name

        # if this logger does'nt exist it will be created 
        # now use logger.info() logger.debug() instead of logging.info() logging.debug() since no more root logger using
        # loggers follow hiearchy if employee does'nt have custom logger it will fall back to Root logger
                # here config follows pattern of root logger? logging.basicConfig() in case logger does'nt have formatter and handler
# to use different config for our custom logger so root logger unaffected 
    # use handler and formatter

# setting log level to custom logger
logger.setLevel(logging.INFO) 

file_handler=logging.FileHandler('53_employee.log')
    # now add this fileHandler to logger above
logger.addHandler(file_handler)

formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    # formatter/formatting is added to file Handler and not to custom logger
file_handler.setFormatter(formatter)


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

#----------------------------------------------------------------------------- 
# logsample.py

import logging
import employee

logger=logging.getLogger(__name__)
        # by convetion use __name__
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler('53_sample.log')
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


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
    result = x / y
    return result



num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

#----------------------------------------------------------------------------- 
# logging only specific level Debugs
        # logsample.py

    # logging level of module set to DEBUG, but if only wanted to log capture to sample.log ERRORS statemetns or wose levels then we can set levels on fileHandlers themselves 
        # file_handler.setLevel(logging.ERROR)
import logging
import employee

logger=logging.getLogger(__name__)
        # by convetion use __name__
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler('53_sample.log')
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


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
    try:
        result=x/y 
    except ZeroDivisionError:
        logger.error('Tried to divide by zero') # to log ERROR
        # to include traceback stack as log use .exception()
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

#-----------------------------------------------------------------------------
# can add multiple handlers to a Logger
    # example in above module log debug statements on console only or separately
            # to log to console only use stream handler
            # to log to separate file use file handler

# logging only specific level Debugs
        # logsample.py

    # logging level of module set to DEBUG, but if only wanted to log capture to sample.log ERRORS statemetns or wose levels then we can set levels on fileHandlers themselves 
        # file_handler.setLevel(logging.ERROR)
import logging
import employee

logger=logging.getLogger(__name__)
        # by convetion use __name__
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler('53_sample.log')
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
    # no need to set log level on this because our logger already has a log level of DEBUG
    # if no explicit formatting added to stream handler it follows by default format when logged
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

logger.addHandler(file_handler)


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
    try:
        result=x/y 
    except ZeroDivisionError:
        logger.error('Tried to divide by zero') # to log ERROR
        # to include traceback stack as log use .exception()
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

# to continue more in docs
    # sending logs via mail
    # rotating logs so one file not filled

#-----------------------------------------------------------------------------
            #-------------------- EXPERIMENT--------------------  


# logs both in console and file?
    # formatting of file different only message
import logging

customLogger=logging.getLogger(__name__)
customLogger.setLevel(logging.INFO)

file_handler=logging.FileHandler('test.log')

# formatter=logging.Formatter('%(asctime)s:%(name)s:%(message)s')


customLogger.addHandler(file_handler)

# also check what is default level later
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')


customLogger.info('info 1')
customLogger.info('info 2')

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # custom logger logs to separate file with simple format , root logger even tho not called logs to separate file with that config format 

            # beech ki bakiyati mat karo , use separate formatter and handlers and levels defined if using custom logger
import logging

customLogger=logging.getLogger(__name__)
customLogger.setLevel(logging.INFO)

file_handler=logging.FileHandler('test.log')

# formatter=logging.Formatter('%(asctime)s:%(name)s:%(message)s')


customLogger.addHandler(file_handler)

# also check what is default level later
logging.basicConfig(filename='rootLog.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')


customLogger.info('info 1')
customLogger.info('info 2')