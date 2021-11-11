import datetime
x=datetime.datetime.now()
# print(x)

#year
# print(x.year)   

#day
print(x.strftime("%A"))   

# y=datetime.datetime(2020,5,17)
# print(y)

#month
# print(y.strftime("%B"))

# eg:   wed,nov 10 ,2021
# %a ---> Wed
# %A --->Wednesday
# %w ---> 3  (sun[0] ,mon[1], tues[2], wed[3])
# %d ---> 10  (day of month)
# %b ---> Nov
# %B ---> November
# %m ---> 11 (month as a no.)
# %y ---> 21 (year)
# %Y ---> 2021
# %p ---> PM  (AM/PM)
