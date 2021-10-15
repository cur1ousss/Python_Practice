# inserting multiple new Lines into vim
	# 77 i ENTER Esc 

# Dates, Times , Timezones, TimeDeltas
	# datetime.datetime , datetime.date , datetime.time
import datetime

# Naive and Aware datetimes
	# naive datetimes - don't have enough info to determine timezone,daylight savings but are easier to work with
	# aware datetimes - Detailed info 

#********************************************************************** 
# Naive datetimes

	# using datetime.date() *******
		# yrs , months ,days
d=datetime.date(2016,7,24)	# no leading zeroes in args otheriwse error pass only integers
print(d)	# leading zeroes automatically added in output

todayy=datetime.date.today()
print(todayy)
print(todayy.year)
print(todayy.day)

# day of the week
print(todayy.weekday())
print(todayy.isoweekday()) 
	# Output isoweekday() = weekday() + 1
		# for weekday()    - Monday is 0 	Sunday is 6
		# for isoweekday() - Monday is 1 	Sunday is 7

# TimeDeltas
	# difference between 2 datetimes
tdelta=datetime.timedelta(days=7)

print(todayy+tdelta)
	# printing date 1 week from now

print(todayy-tdelta)
	#printing date 1 week ago

# Date +/- TimeDelta = Another Date
# Date +/- Date = TimeDelta

birthday=datetime.date(2022,9,24)
days_till_Bday= birthday-todayy
print(days_till_Bday)
print(days_till_Bday.days)
print(days_till_Bday.total_seconds())


	# using datetime.time()  ************
import datetime
	# hrs mins secs and microsecs
		# by default does'nt has timezone info so is still Naive but can specify timezone using tz_info
t=datetime.time(9,30,45,1000)
print(t)
print(t.hour)
	# datetime.time is Less used

# using datetime.datetime ************
	# gives all info date and time
dt=datetime.datetime(2016,7,26,12,30,45,1000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)	# dt.year is year attribute dt.time() is time() function()
			# hence dt.time gives only address of calling no real output 
print(dt.time)

tdelta=datetime.timedelta(hours=12)
print(dt+tdelta)

	# datetime.datetime constructors
dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utc_now=datetime.datetime.utcnow()

print(dt_today)
print(dt_now)		# datetime.today() and datetime.now() similar output only Microsecond diffrence because of execution
	# datetime.today() vs datetime.now()  .now() allows TimeZone as argument .today() has None timezone 
print(dt_utc_now)	# gives current UTC time but tz_info is still null/none by default

#***************************************************************************** 

# pip install pytz - pytz library is more useful 3rd party recommended by pydocs

# timezone aware datetime from now

import datetime
import pytz

	# recommended to work with UTC timezone
dt=datetime.datetime(2016,7,27,12,30,45,tzinfo=pytz.UTC)
print(dt)	# op - 2016-07-27 12:30:45+00:00   + 00 is UTC offset

dt_now=datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utc_now=datetime.datetime.utcnow()
	# bydefault has no arg to pass as tzinfo UTC
dt_utc_now=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utc_now)

	# datetime.now(tz=UTC) preferred over datetime.utcnow().replace(tzinfo=pytz.UTC) since more readable


dt_utc_now=datetime.datetime.now(tz=pytz.UTC)
print(dt_utc_now)

# Converting Timezones using givenTime.timezone(pytz.timezone(''))
print(pytz.all_timezones)	# list of all timezones in pytz

dt_india=dt_utc_now.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_india) # offest is +5.30 time difference between my timezone and UTC timezone

# making naive time -> timezone aware
dt_mtn=datetime.datetime.now()
print(dt_mtn)

dt_east=dt_mtn.astimezone(pytz.timezone('US/Eastern')) # ? Error should cannot convert naive datetime .astimezone() cannot be applied to naive datetime
	# dt_mtn = datetime.datetime.now
	# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))

	# This was an error in the video around 21:22. In Python 3.6 this is not an error anymore and according to the official docs:
	# The astimezone() method can now be called on naive instances that
	# are presumed to represent system local time. https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25
print(dt_mtn)

# using localise() function for timezone conversion on naive datetime
date_mountain=datetime.datetime.now() # naive datetime
mountain_timezone=pytz.timezone('US/Mountain')

date_mountain=mountain_timezone.localize(date_mountain) # making naive datetime timezone aware
print(date_mountain)
	# now can convert timezone aware datetime to another timezone

#***************************************************************************** 

# passing date times and display
import datetime
import pytz

date_mntn=datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
	# use ISO format - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(date_mntn.isoformat())

# strftime() for format codes of datetime formatting
print(date_mntn.strftime('%B %d ,%Y'))

# Convert String to DateTime
	# strptime()
dateString='July 16,2016'
newDate=datetime.datetime.strptime(dateString,'%B %d,%Y')
print(newDate)

	# strftime -> Datetime to String	
			# f stands for format
	# strptime -> String to Datetime
			# p stands for parse

# Future - Arrow module Python also used for advanced datetime management
	# https://arrow.readthedocs.io/en/latest/
	# https://pypi.org/project/arrow/