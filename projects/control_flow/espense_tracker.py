# @title 17. Basic Expense Tracker
"""
An Expense Tracker is a practical application that
allows users to log their daily expenses and track spending
habits. This project enhances knowledge of file handling,
data storage, and user input processing in Python.
This chapter covers the step-by-step implementation of an
Expense Tracker, including user input handling, data storage
in a CSV file, and displaying expense reports.

Key Concepts of Expense Tracker in Python

Data Handling:

Using lists and dictionaries to store
expenses
Writing and reading data from a CSV file

User Input Processing:

Taking user input for expense details
Validating and formatting input data

Report Generation:

Displaying total expenses per category
Summarizing daily or monthly spending

"""

import csv
from pathlib import Path


workfile = Path("expense_tracker")
workfile.mkdir(exist_ok=True)
file_path = workfile / "expense.csv"
header = ["Amount", "Date", "Category"]

def save_expenses(fil_path, expenses):
    file = Path(fil_path)
    file_exist = file.exists()
    with open(file, "a", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
    
        if not file_exist:
            writer.writeheader()
        writer.writerow(expenses)
        print("Expenses added succesfully")

def load_expenses(fil_path):
    file = Path(fil_path)
    file_exist = file.exists()
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

try:
    amount = float(input("Enter amount: "))
    date = input("Enter the date of the transaction: ")
    category = input("Enter the category of your expense: ")

    expenses = {
        "Amount": amount,
        "Date": date,
        "Category": category
    }

    save_expenses(file_path, expenses)



except ValueError:
    print("Invalid input")
