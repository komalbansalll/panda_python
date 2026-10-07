# modules
import test
# print (test.data())

print (test.add(20,30))

 
# print(test.add(10, 20))
# print(test.subtract(20, 5))
# print(test.multiply(5, 4))

print (test.name)
print(test.age)
print(test.course)


print(test.abc[2]) #index number if i want 1 name to print 

import datetime 
now = datetime.datetime.now()
print(now)

today = datetime.date.today()
print (today)

t = datetime.datetime.now ()
print(t.year)
print(t.day)
print(t.month)
print(t.hour)
print(t.minute)
print(t.second)

# calender
import calendar
# print(calendar.calendar(2026)) 
print(calendar.month(2026,10))
print(calendar.isleap(2026))
print(calendar.weekday(2026,10,7)) #counts from 0 = monday
print (calendar.setfirstweekday(calendar.SUNDAY))
print ("firstweekday:",calendar.month(2026,10))
print("monthrange:",calendar.monthrange(2026,11))
print("monthcalendar:",calendar.monthcalendar(2026,10))

import math
print(math.sqrt(25))
print(math.pow(2,3))
print (math.floor(3.9))

# user deifined function
print (2**3)

# sqrt(), pow(), ceil(), floor(), factorial(), gcd(), lcm()
print(math.ceil(3.9))
print(math.factorial(5))
print(math.gcd(12, 18))
print(math.lcm(12, 18))
print(math.pi)
# Take the base and height of a right triangle and find the hypotenuse using math.sqrt().
base = 3
height = 4
result = math.hypot(base, height)
print (result)

# Take an angle in degrees and convert it to radians using math.radians().
angle = 45 
result = math.radians(angle)
print(result)
# Take a negative number and find its absolute value using math.fabs().
number = -9
result = math.fabs(number)
print("fabs:",result)
