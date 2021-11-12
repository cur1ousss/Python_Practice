import datetime
import calendar

# script to find months to pay credit bill
	# constraint keep in mind monthly_payment must be greater than interest otherwise will be stuck infinite loop failing to pay interest only
credit_balance=5000
interest_rate=13*0.1 # || interest_rate=0.13
monthly_payment=500

today=datetime.date.today()
# to find next first day of month as payment made on 1st of every upcoming month
days_in_current_month=calendar.monthrange(today.year,today.month)
			# monthrange returns tuple (index of day,total days in month)
print(days_in_current_month)

days_in_current_month=calendar.monthrange(today.year,today.month)[1]	# accessing first element of returned tuple

day_till_end_of_month=days_in_current_month - today.day
print(day_till_end_of_month)

start_date=today+datetime.timedelta(days=day_till_end_of_month+1)
print(start_date)

end_date=start_date

while credit_balance>0:
	interest_charge=(interest_rate/12)*credit_balance
	credit_balance+=interest_charge

	credit_balance-=monthly_payment

	credit_balance=round(credit_balance,2)
	if credit_balance<0:
		credit_balance=0
	
	# using ternary operator short above lines
	credit_balance=0 if credit_balance<0 else round(credit_balance,2)

	print(end_date,credit_balance)

	days_in_current_month=calendar.monthrange(end_date.year,end_date.month)[1]
	end_date=end_date+datetime.timedelta(days=day_till_end_of_month)
		# to carry over into next month

#***************************************************************************** 

# weeks to lose weight
import datetime

current_weight=220
goal_weight=180

lose_per_week=1.5

start_date=datetime.date.today()
end_date=start_date

while current_weight>goal_weight:
	end_date+=datetime.timedelta(days=7)
	current_weight-=lose_per_week

print(f'reached goal in {(end_date-start_date).days//7} on {end_date}')

#***************************************************************************** 

# sub goal every day
import datetime
import math

goal_subs=100000
current_subs=85000

subs_to_go=goal_subs-current_subs

avg_subs_day=200
days_to_go=math.ceil(subs_to_go/avg_subs_day)

today=datetime.date.today()
print(today+datetime.timedelta(days=days_to_go))