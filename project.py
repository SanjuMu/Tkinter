from tkinter import *
from datetime import datetime

root =Tk()
root.title("Age Calculator App")
root.geometry("400x400")

def calculate_age():
    name = name_entry.get()
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    
    birth_date = datetime(year, month, day)
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    message = "Hello {}, you are {} years old!".format(name, age)
    ("Age Calculator", message)

Label(root, text="Name:")
name_entry = Entry(root)


Label(root, text="Day:")
day_entry = Entry(root)

Label(root, text="Month:")
month_entry = Entry(root)

Label(root, text="Year:")
year_entry = Entry(root)

calculate_button = Button(root, text="Calculate Age", command=calculate_age)

root.mainloop()

# Note to teacher: I am not sure how to function this