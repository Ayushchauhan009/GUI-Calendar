from tkinter import *
import calendar
root = Tk()
root.title("My own GUI calender")
year = 2021
myCal = calendar.calendar(year)
cal_year = Label(root, text=myCal, font="Consolas 10 bold")
cal_year.pack()
root.mainloop()
