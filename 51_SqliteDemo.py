# sqliteDemo.py >>
import sqlite3

con=sqlite3.connect(':memory:')
    # in connect() can pass file where we want to store our data or we can make in memory database :memory:
con=sqlite3.connect('51_employee.db')
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

# to iterate through returned result of select command
print(c.fetchone())
    # will get the next row in our results and only return that row , if no more rows available returns None
print(c.fetchmany(5))
    # returns that number of rows as a list
    # if no more rows available returns an empty list

print(c.fetchall())
    # returns rows as list
    # if no more rows left returns an empty list


print(c.fetchone())
property(c.fetchall())

c.execute("INSERT INTO employees VALUES ('Corey','Schafer',50000)")
c.execute("SELECT * FROM employees WHERE LAST='Schafer'")
    # when run select() statement below insert automatically auto commits our insert transaction above
        # can also explicitly con.commit() between insert and select
            # but compulsory to con.commit() incase no select statements exist

con.commit() # not cursor c.commit() 
    # commits the current transaction

con.close()
    # close connection to database / close resources

#----------------------------------------------------------------------------- 

    # using custom names to stuff into database

from 51_SqliteEmployee import Employee  # red since module name can't start with numbers or _
import sqlite3

conn=sqlite3.connect('51_employee.db')

c=conn.cursor()

emp1=Employee('John','Doe',80000)
emp2=Employee('Jane','Doe',90000)

print(emp1.first)
print(emp1.pay)

# adding emp1 to database
    # one would think to put like stream/string formatting using {} placeholders
c.execute("INSERT INTO employees VALUES('{}','{}','{}')".format(emp1.first,emp1.last,emp1.pay))
    # Bad practice while dealing with Databases
        # since Vulnerable to SQL Injection attacks
# better method
    # use DB API placeholder -> '?' question marks
c.execute("INSERT INTO employees VALUES(?,?,?)",(emp1.first,emp1.last,emp1.pay))
        # pass placeholders as tuples arguments
            # even if single placeholder pass single value as a tuple (value,) {extra , comma remains to identify as tuple} as argument the value

# best method used by Corey
    # use colon and name of placeholder
        # :first,:last,:pay and pass Dictionary argument with previous given name of placeholders as key and their values as the value to pass stuff into db
c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{"first":emp1.first,"last":emp1.last,"pay":emp1.pay})


# Select statement for custom values find
c.execute("SELECT * FROM employees where last=?",('Schafer',))
            # ? question mark placeholder from DB API 
                # passing even single value as tuple ('schafer',) extra comma remains to identify as tuple format convetion by default


c.execute("SELECT * FROM employees where last=:last",{'last':emp2.last})
c.execute("SELECT * FROM employees where last=:last",{'last':"Doe"})
            # using :name colon placeholderName and dictionary as argument  

#----------------------------------------------------------------------------- 
# Making database that lives in RAM
    # useful for testing if want fresh clean database on every run
        # using keyword :memory: in connect() parameter of connection
import sqlite3

connection=sqlite3.connect(':memory:')
    # also we don't get table already exists (like above need to comment some statements while running others) error since everytime run new fresh start
    # also insert statemenets overwrite older insert statement data in database

#----------------------------------------------------------------------------- 
# making functions to insert delete emp
import sqlite3

con=sqlite3.connect('51_employee.db')

c=con.cursor()

c.execute("""CREATE TABLE employees(
    first text,
    last text,
    pay integer
    )""")

def insertEmp(emp):
   c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{"first":emp.first,"last":emp.last,"pay":emp.pay})
# need commit() after every insert update hence use sqlite connection objects and context managers to automate resources

# context managers are a way to setup and teardown resources automatically
    # with sqlite connection objects can be used as context managers that automatically commit or rollback transactions so transactions will automatically be committed unless theres an exception then it will be automatically rolled back 
def insertEmp(emp):
    with con:
        c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{"first":emp.first,"last":emp.last,"pay":emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees where last=:last",{'last':lastname})
        # select statements don't need to be committed hence no need of context managers using connection object
    return c.fetchall()

def update_pay(emp):
    with conn:
        c.execute("""update employess set pay=:pay where first=:first and last=:last""",{'first':emp.first,'last':emp.last,'pay':emp.pay})

def remove_emp(emp):
    with conn:
        c.execute("delete from employees where first=:first and last=:last",{"first":emp.first,"last":emp.last})

emp1=Employee('John','Doe',80000)
emp2=Employee('Jane','Doe',90000)

insertEmp(emp1)
insertEmp(emp2)

emps=get_emps_by_name('Doe')
print(emps)

update_pay(emp2,95000)
remove_emp(emp1)


con.close()

#-----------------------------------------------------------------------------
# SQLite also works with SQLalchemy
    # sqlalchemy is ORM for python that abstracts away a lot of differences between databases 
    # can use sqlalchemy with sqlite to get everything prototyped out in your application and when youre ready can easily replace that postgres or mysql without changing much code