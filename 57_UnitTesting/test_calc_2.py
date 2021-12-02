import unittest
from unittest import result
import calc_1

# create testcases for functions that we want to test
    # in order to create those test cases create test class that inherits from unittest.TestCase 

class testCalc(unittest.TestCase):

    # convention to name starting with test_whatTesting method
        # test_sub() test_add()
            # add_test() would'nt work altho compile but no tests will be performed when testing > python -m unittest moduletest.py
    def test_add(self):
        # https://docs.python.org/3/library/unittest.html#assert-methods
            # since inherited from unittest.TestCase have access to assert method 
        result=calc_1.add(10,5)
        self.assertEqual(result,15)

    def test_addFailDeliberate(self):
        result=calc_1.add(10,5)
        self.assertEqual(result,14)


# OUTPUT {running unit test on terminal separately by passing unittest module}
    # TO RUN
    # > python -m unittest moduleToTest.py

# to use shorter python moduleToTest.py directly instead of python -m uniitest moduletoTest.py use if __name__==__main__
if __name__=='__main__':
    unittest.main()

#############################################################################
class testCalc(unittest.TestCase):

    def test_add(self):
        result=calc_1.add(10,5)
        self.assertEqual(result,15)

    def test_addFailDeliberate(self):
        result=calc_1.add(10,5)
        self.assertEqual(result,14)

    def test_add_edgeCases(self):
        self.assertEqual(calc_1.add(10,5),15)
            # can also directly use method returned value call in assert() method
        self.assertEqual(calc_1.add(1,-1),0)
        self.assertEqual(calc_1.add(-1,-1),-2)
                # counts as 1 test not 3 tests in final console, since final test count is count of test methods
if __name__=='__main__':
    unittest.main()

# a single method is 1 test
    # in a method u can have many tests but that are not counted in whole tests


##############################################################################
# adding all test methods

import unittest
import calc_1


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc_1.add(10, 5), 15)
        self.assertEqual(calc_1.add(-1, 1), 0)
        self.assertEqual(calc_1.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc_1.subtract(10, 5), 5)
        self.assertEqual(calc_1.subtract(-1, 1), -2)
        self.assertEqual(calc_1.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc_1.multiply(10, 5), 50)
        self.assertEqual(calc_1.multiply(-1, 1), -1)
        self.assertEqual(calc_1.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc_1.divide(10, 5), 2)
        self.assertEqual(calc_1.divide(-1, 1), -1)
        self.assertEqual(calc_1.divide(-1, -1), 1)
        self.assertEqual(calc_1.divide(5, 2), 2.5) # to check floor division fault
        
    # to check division by zero 0 error use 2 approach >>
        # 1st not preferred by corey
        self.assertRaises(ValueError,calc_1.divide,10,0)   
            
        # 2nd calling the function using context manager and handling the error
        with self.assertRaises(ValueError):
            calc_1.divide(10,0)
                # when testing exceptions context manager preferred by corey



if __name__ == '__main__':
    unittest.main() 

# in case of multiple tests
    # output is of form 
        # ..F. -> meaning 1234 cases and 3rd F failed
