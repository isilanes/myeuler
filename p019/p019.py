'''
You are given the following information, but you may prefer to do some research for yourself.

  * 1 Jan 1900 was a Monday.
  
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  
  * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

#-------------------------------------------------------------------------#

def f1():
    days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] # per month
    first_day = 5 # 0 = monday, 6 = sunday; Jan 1, 1900 was a monday

    sundays = 0
    for year in range(1901,2001):
        cdays = days[:] # copy of days (to modify freely if leap)

        # Is it leap year:
        leap = False
        if not year % 400:
            leap = True
        elif not year % 100:
            leap = False
        elif not year % 4:
            leap = True

        if leap:
            cdays[1] = 29

        # Loop over months:
        for month in range(12):
            first_day += cdays[month-1]
            first_day = first_day % 7
            if first_day == 6:
                sundays += 1

    return sundays

#-------------------------------------------------------------------------#

res = f1()

print(res)
