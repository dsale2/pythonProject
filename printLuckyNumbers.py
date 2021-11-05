import datetime
import tkinter as tk
from PIL import Image,Image
# coding=utf-8

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Dan')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0]

lucky_numbers[0] = 90
for x in lucky_numbers:
    print (x)
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))

colour = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print(+ "Roses are", colour)
print(pluralNoun + " are blue")


