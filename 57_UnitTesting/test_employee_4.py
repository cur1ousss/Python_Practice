from types import resolve_bases
import unittest
from unittest import mock
from employee_3 import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'
            # chaning first name to check if dynamically email also changes as should acc to previous code being tested
        self.assertEqual(emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)

if __name__=='__main__':
    unittest.main()

#############################################################################
# goal is to make code DRY
    # DRY - don't repeat yourself automate/subsitute earlier value where possible
        # example here creating same object multiple times code repeated

# use setup and teardown methods
    # to create objects to be tested upon in one place
        # use setUp() and tearDown()

# setUp method will run its code before every single test
    # created before every single test so modifications of one test won't affect another shared instance value
# tearDown method will run its code after every single test
    # usecase of teardown if some function making folders,files,and databases use tearDown to clean delete them start from clean slate

    # order of running 
        # setUp1
        # testcase1
        # teardown1 and so on 

    # tests are not run in order of running hence keep tests independent of another altho can call explicitly one inside another if needed

import unittest
from employee_3 import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
            # emp_1 = Employee('Corey', 'Schafer', 50000)
            # emp_2 = Employee('Sue', 'Smith', 60000)
        # to access these in other tests make them instance attributes unlike above where scope limited to each test
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
            # chaning first name to check if dynamically email also changes as should acc to previous code being tested
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

if __name__=='__main__':
    unittest.main()

#############################################################################

# setUp and tearDown run before and after every single test
    # to run once before everything and once after everything use setupclass and teardownClass() are class methods working with the class not instance
# setUpClass() and tearDownClass() used when need something to run only once which would be costly if run for every single test
    # example populate a database,reading db

# order of running
    # setUpClass()
    # setUp
    # test
    # tearDown
    # setUp2
    # test2
    # tearDown2

    # tearDownClass()

import unittest
from employee_3 import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
            # emp_1 = Employee('Corey', 'Schafer', 50000)
            # emp_2 = Employee('Sue', 'Smith', 60000)
        # to access these in other tests make them instance attributes unlike above where scope limited to each test
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
            # chaning first name to check if dynamically email also changes as should acc to previous code being tested
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

if __name__=='__main__':
    unittest.main()

#############################################################################

# if code relies on things that we have no control over
    # example if site down then fetch fails function fails test fails but not fault of our code hence get around this with "Mocking"

    # employee.py
import requests

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self,month):
        response=requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

# so information from that website is something we might wanna mock because we don't want success of our tests to depend on that site being up we only care if get method was called with the correct URL and our code behaves correctly whether response is ok or not ok
# so import from mock patch
    # ways of using patch
        # as a decorator
        # as a context manager
    # will allow us to mock an object during test and then object automatically restored after test is run

        # test_employee.py  
import unittest
from unittest.mock import patch # importing patch
from employee_3 import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
            # emp_1 = Employee('Corey', 'Schafer', 50000)
            # emp_2 = Employee('Sue', 'Smith', 60000)
        # to access these in other tests make them instance attributes unlike above where scope limited to each test
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)
        
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
            # chaning first name to check if dynamically email also changes as should acc to previous code being tested
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            # using patch as context manager
            # $yntax 
                # with patch('whatWantToMock') as alias:
                    #  requests.get of employee module so employee.requests.get
                # reason not used requests in test.py since we want to mock these objects from where they're actually used in employee.py
            mocked_get.return_value.ok=True
            mocked_get.return_value.text='Success'
                    # .ok and .text are attributes of reponse object
            
            schedule=self.emp_1.monthly_schedule('May')
            # mock objects record when they were called and with what values
            
            # we want to make sure that get method was called with a correct URL 
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule,'Success')

            #### for failed Response
            mocked_get.return_value.ok=False
            
            schedule=self.emp_2.monthly_schedule('June')
            # mock objects record when they were called and with what values
            
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule,'Bad Response!')


if __name__=='__main__':
    unittest.main()

#############################################################################
# best practices
    # tests should be isolated indenpendent of each others failures/successes

# future
    # pytest vs unittest