"""
birthday.py
Author: MaCucyrt07 
Credit: Ella, Kyle
Assignment: Birthday Quiz

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month = month_name[todaymonth]
name = input("Hello, what is your name? ")
print("Hi",name+", what was the name of the month you were born in?")
b = birthmonth = input()
print("And what year were you born in,",name+"?")
a = birthyear = float(input())
print("And the day?")
c = birthday = float(input())

if b == 'October' and c == 31:
    print ("You were born on Halloween!")
elif b == month and c == todaydate:
    print ("Happy Birthday!")



else:
    if b in ['March','April','May']:
        season = 'spring'
    elif b in ['December','January','February']:
        season = 'winter'
    elif b in ['June', 'July', 'August']:
        season = 'summer'
    elif b in ['September','October','November']:
        season = 'fall'
    
    if a<=1979:
        age = 'Stone Age.'
    elif a<=1989:
        age = 'eighties.'
    elif a<=1999:
        age = 'nineties.'
    elif a<=2020:
        age = 'two thousands.'
    
    print (name+', you are a',season,'baby of the',age)
