#Tyson Vorwaller
#9/18
#Clock

#1 Import time & calendar & invoke calendar.timegm
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime

def current_time():
    total_mil_sec = calendar.timegm(time.gmtime())*1000 
    total_sec = total_mil_sec // 1000
    cur_sec = total_sec % 60
    total_min = total_sec // 60
    cur_min = total_min % 60
    total_hrs = total_min // 60
    cur_hrs = total_hrs % 24

    

#set the time zone
    cur_hrs = cur_hrs - 6

    if cur_hrs >=12:
        tag="PM"
    else:
        tag="AM"
#format the output
    timex = str(cur_hrs)+":"+ str(cur_min)+":"+str(cur_sec)+tag
    a = 30
    if cur_sec == a:
        beep()
    return timex
x=current_time()
print(x)

def beep():
  winsound.Beep(540,80000) 

def quit(*args):
    root.destroy()

def show_time():
    time = current_time()
    txt.set(time)
    root.after(1000, show_time)

root = Tk()
root.attributes("-fullscreen",True)
root.configure(background='Dark blue')
root.bind("q",quit)
root.after(1000, show_time)
fnt = font.Font(family='Papyrus', size=100, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="Blue", background="light blue")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
                











