import datetime
import math

import tkinter as tk
from PIL import Image, Image, ImageTk

window = tk.Tk()
window.geometry("620x780")
window.title(" How old am I? ")

name = tk.Label(text="Name*")
name.grid(column=0, row=1)
date = tk.Label(text="Day of Month*")
date.grid(column=0, row=2)
month = tk.Label(text="Month in Year*")
month.grid(column=0, row=3)
year = tk.Label(text="Year*")
year.grid(column=0, row=4)

nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=4)

def getInput():
    name = nameEntry.get()
    if not name:
        answer = " Name is a required field"
    else:
        person = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
        answer = "Heyy {person}!!!.\n" \
                 "{ageInYearsMonthAndDays}\n" \
                 "That's a total of:\n  - {ageInDays} days\n  - {ageInMonths} months\n  - {ageInYears} years".format(
            person=name, ageInDays=person.ageInDays(), ageInMonths=person.ageInMonths(), ageInYears=person.ageInYears(),ageInYearsMonthAndDays=person.ageInYearsMonthAndDays())

    textArea = tk.Text(master=window, height=10, width=75)
    textArea.grid(column=1, row=6)
    textArea.insert(tk.END, answer)

button = tk.Button(window, text="Calculate Age", command=getInput, bg="pink")
button.grid(column=1, row=5)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def ageInDays(self):
        today = datetime.date.today()
        ageInDays = abs((today - self.birthdate).days)
        return ageInDays

    def ageInMonths(self):
        today = datetime.date.today()
        ageInMonths = abs(12/365.25 * (today - self.birthdate).days)
        return ageInMonths

    def ageInYears(self):
        today = datetime.date.today()
        ageInYears = abs((today - self.birthdate).days/365.25)
        return ageInYears

    def ageInYearsMonthAndDays(self):
        today = datetime.date.today()
        ageInYears = abs((today - self.birthdate).days/365.25)
        ageInWholeYears = int(ageInYears)
        remainingAgeInMonths = ageInYears-ageInWholeYears;
        remaingAgeInWholeMonths = int(math.floor(12*remainingAgeInMonths));
        remaingAgeInDays = int((365*remainingAgeInMonths) - (365*(math.floor(12*remainingAgeInMonths)/12)));

        age = "You are {ageInWholeYears} years, {remaingAgeInWholeMonths} months & {remaingAgeInDays} days old.".format(
            ageInWholeYears=ageInWholeYears, remaingAgeInWholeMonths=remaingAgeInWholeMonths, remaingAgeInDays=remaingAgeInDays)

        return age


image = Image.open('age.jpeg')
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

window.mainloop()
