import random
from tkinter import *
from tkcalendar import Calendar
from tkinter import ttk

tk = Tk()

''' UI Interface '''
tk.geometry("400x400")
style = ttk.Style(tk)
style.theme_use('clam')
tk.title("Simplilearn Dice")

label = Label(tk, text="", font=("times", 260))


def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683']
    label1 = label.configure(
        text=f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
    label.pack()


button = Button(tk, text="Let's Roll...", width=40, height=6, font=11, bg="white", command=roll)
button.pack(pady=10)

label1 = Label(tk, text="© 2009-2023 - Simplilearn Solutions. All Rights Reserved.")
label1.pack(pady=20)

tk.mainloop()
