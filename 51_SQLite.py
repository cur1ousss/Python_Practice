# useful for small medium applications database and prototyping 
# part of standard library

# database can be 
    # a simple file
    # or a in memory database that lives in ram

# employee.py >>
class Employee:
    """A sample Employee class"""

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)



# sqliteDemo.py >>
import sqlite3

con=sqlite3.connect(':memory:')
    # in connect() can pass file where we want to store our data or we can make in memory database :memory:
con=sqlite3.connect('employee.db')
        # if not exists creates .db in same directory
        # if exists then just connects not overwrite

# cursor helps execute sql commands 
    # cursor c below
c=con.cursor()

# run sql commands using execute() method
    # use docstring to pass command since syntax maintained no unexpected newlines
    # for single line commands can use simple "" quotes like string no need docstring
c.execute("""CREATE TABLE employees(
    first text,
    last text,
    pay integer
    )""")
    # columnName DataType
    # limited datatypes in sqlite 
        # https://www.sqlite.org/datatype3.html

c.execute("INSERT INTO employees VALUES ('Corey','Schafer',50000)")

c.execute("SELECT * FROM employees WHERE LAST='Schafer'")

# to iterate through returned result
c.fetchone() 
    # will get the next row in our results and only return that row , if no more rows available returns None
c.fetchmany(5)
    # returns that number of rows as a list
    # if no more rows available returns an empty list

c.fetchall()
    # returns rows as list
    # if no more rows left returns an empty list


print(c.fetchone())
property(c.fetchall())

c.execute("INSERT INTO employees VALUES ('Corey','Schafer',50000)")
c.execute("SELECT * FROM employees WHERE LAST='Schafer'")
    # when run select() statement below insert automatically auto commits our insert transaction above
        # can also explicitly con.commit() between insert and select

con.commit() # not cursor c.commit() 
    # commits the current transaction

con.close()
    # close connection to database / close resources