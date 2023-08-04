from tkinter import *          
from tkcalendar import*
from datetime import datetime

root = Tk()
root.title("CALENDAR")
root.geometry('600x500')
root.configure(bg="lightgreen")

my_cal=Calendar(root,setmode="day",date_pattern="d/m/yy")
my_cal.pack(pady=1) 


def get_date():
    selectdate = my_cal.get_date()
    Datename = datetime.strptime(selectdate,"%d/%m/%y")
    Datename_diff = Datename.strftime("Selected Date: %d %B %Y")
    cal_label.configure(text= Datename_diff,font=("Bold", 15, "bold"))

cal_label=Label(root,background="pink")
cal_label.pack(pady=15)
btn=Button(root, text = 'SELECT DATE',  background = "white", fg = "black",command = get_date)
btn.pack(side = 'top')  
btn.pack(pady=15) 

root.mainloop()