#!/bin/python3
from datetime import datetime
for _ in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t1-t2).total_seconds())))


#2nd solution
import calendar
import operator
from time import strptime
def parseTime(str):
    ops = { "+": operator.sub, "-": operator.add } 
    spl = str.rsplit(" ",1)
    t = strptime(spl[0], "%a %d %b %Y %H:%M:%S")
    tz = ops[spl[1][0]](0,int(spl[1][1:3]) * 3600 + int(spl[1][3:]) * 60)
    return calendar.timegm(t) + tz
for _ in range(int(input())):
    print(abs(parseTime(input()) - parseTime(input())))