# str() vs repr()

from types import CodeType


a=[1,2,3,4]
b='sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

# str a     [1, 2, 3, 4] 
# repr a    [1, 2, 3, 4] 
# str b     sample string
# repr b    'sample string'


# str() returns a string containing nicely printable represenation of an object, for strings returns the string itself 
    # repr() vs str() -> str() does'nt always attempt to return a string that is acceptable to eval() , its goal is to return a printable string if no argument is given it returns a empty string
    # repr() returns a string containing printable representation of an object , is the same value yielded by conversions{reverse quotes} 1:59 more text >> https://www.youtube.com/watch?v=5cvM-crlDvg

# goal of repr() is to be unambiguous
# goal of str() is to be readable


# example
    # >> can run output of repr() as py code 

import datetime
import pytz

a=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b=str(a)

print(f'str(a) {str(a)}')
print(f'str(b) {str(b)}')

print(f'\nrepr(a) {repr(a)}')
print(f'repr(b) {repr(b)}')


# str(a) 2021-11-23 17:09:23.271332+00:00
# str(b) 2021-11-23 17:09:23.271332+00:00

# repr(a) datetime.datetime(2021, 11, 23, 17, 9, 23, 271332, tzinfo=<UTC>)
# repr(b) '2021-11-23 17:09:23.271332+00:00'    
        # repr() helps to find doodh ka doodh paani ka paani makes them unambiguos finds amogos

# repr() meant for debugging
    # example if value returned from database help convert that check 
            # since str() value will be same , repr() will help find amogus