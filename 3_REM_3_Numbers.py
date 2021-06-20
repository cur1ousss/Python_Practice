
# REMAINING >>> ????? Rounding OFF Confusion how rounding off works off?


Variable_num=3
float_num=31.42

print(type(Variable_num))  # type(someVariable)  prints out class of dataType of Variable
print(type(float_num))

# *****************************************************************************

    #  OPERATORS

# Arithmetic Operators
    # +  addition
    # -  subtraction 
    # *  multiplicatioN

# Division
    # 3/2 = 1.5 for Python 3
    # 3/2 = 1   for Python 2
    
    # 3//2 = 1  Floor Division for Python3

# Exponent | Power of 
    # a**b  
    #  3**2 = 9

# Modulo
    # 3%2 = 1  Modulo %  >> gives remainder after division

# +=    >> num+=num is num=num+num
# -=
# *=
# /=

# *****************************************************************************

# abs() Absolute value
print(abs(-3))

# *****************************************************************************

# round() Rounds off value to closest integer
    # round(Number,Digits) >> {Digits >> How many digits after Decimal Point Default is Zero (0)}
    
    # round(Number) >> rounds of to closest Integer Whole number

print(round(5.76543,2))    # >> 5.77
print(round(3.5))

print(round(3.0532,1))  # 3.1
print(round(3.05))      # 3

# *****************************************************************************

# Round off to closest Even Integer For Single Digit Decimals only?
    # 0.5 >> 0
    # 1.5 >> 2
    # 2.5 >> 2
    # 3.5 >> 4

# Rounding off Multi Digit Decimals
    # 4.50 >> 4
    # 4.51 , 4.52 >> 5  {Normal Logic}


# For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the ** EVEN CHOICE ** (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). Any integer value is valid for ndigits (positive, zero, or negative). The return value is an integer if ndigits is omitted or None. Otherwise the return value has the same type as number.

# *****************************************************************************

    # Numbers in the form of string

numx='100'
numy='200'

print(numx+numy) # gives 100200 since strings with "+" operator are concatenated


# Casting Integer like String to Integer
    # variableX=int(variableX)
    # variableX=int(varibleY)
    # variableX=int(StringLikeNumber)
num1='100'
num2='200'

num1=int(num1)
num2=int(num2)
print(num1+num2)
