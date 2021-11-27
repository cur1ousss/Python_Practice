# employee.py >>
class Employee:
    """A sample Employee class"""

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)