# Memoization refers to the mechanism that makes a function not having to compute the output using an input, when the function has been executed using the same input before. This is possible because the computer memorizes the input:output pair.

# This tool can be demonstrated in python using an if statement and a dictionary outside the function.

import time

def expensive_func(num):
    print("Computing {}...".format(num))
    time.sleep(1)
    result = num*num
    return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

	# using Memoization to improve performance above execs in 4 secs below memoized execs in 2 secs
import time

ef_cache = {}

def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Computing {}...".format(num))
    time.sleep(1)
    result = num*num
    ef_cache[num] = result
    return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)