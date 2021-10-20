import math
def is_leap(x):
    if year%4==0 and year%400==0 and  year%100==0:
        return True
    else:
        return False
year=int(input())
y=is_leap(year)
print(y)