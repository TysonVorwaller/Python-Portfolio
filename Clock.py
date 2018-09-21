#Tyson Vorwaller
#9/18
#Clock

#1 Import time & calendar & invoke calendar.timegm
import time
import calendar

def clock():
    total_mil_sec = calendar.timegm(time.gmtime())*1000
    total_sec = total_mil_sec // 1000
    cur_sec = total_sec % 60
    total_min = total_sec // 60
    cur_min = total_min % 60
    total_hrs = total_min // 60
    cur_hrs = total_hrs % 24

    return cur_sec,cur_min,cur_hrs
while True:
    s,m,h=clock()
    print(h,m,s)













