from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk


tk = Tk()

''' UI Interface '''
tk.geometry("400x400")
style=ttk.Style(tk)
style.theme_use('clam')
tk.title("Simplilearn Calender")

''' Default Calender '''
cal=Calendar(tk, selectmode='day', year=2023, month=1,day=11)
cal.pack(pady=20, fill="both", expand=True)

''' Custom Calender '''
def date_Picker():
    date.config(text="Selected Date is :"+cal.get_date())

Button(tk,text="Get Date",command=date_Picker).pack(pady=20)

date=Label(tk,text="© 2009-2023 - Simplilearn Solutions. All Rights Reserved.")
date.pack(pady=20)


tk.mainloop()