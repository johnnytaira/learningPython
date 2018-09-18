#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime
from datetime import date
# ano corrente
now = date.today().year

name = input("Gimme your name: ")
print("Your name is: " + name)

age = input("Gimme your age: ")
age = int(age)

print(name + " will be hundred at age " + str((now - age) + 100))
