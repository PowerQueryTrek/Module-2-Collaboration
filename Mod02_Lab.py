# Module 2 Lab - Case Study: if...else and while
# Brian D. Paasch
# file name = Mod02_Lab.py
# find this file at https://github.com/PowerQueryTrek/Module-2-Collaboration 
# This Python app that will accept student names and GPAs and test if the student qualifies
# for either the Dean's List or the Honor Roll.

lname = input("Please enter student's last name (enter 'ZZZ' to quit): ")

while lname.upper() != 'ZZZ':
    fname = input("Please enter student's first name: ")
    gpa = float(input("Please enter student's GPA: "))

    if gpa >= 3.5:
        print(f"{fname} {lname} qualifies for the Dean's List.")
    elif gpa >= 3.25:
        print(f"{fname} {lname} qualifies for the Honor Roll.")
    
    lname = input("Please enter student's last name (enter 'ZZZ' to quit): ")