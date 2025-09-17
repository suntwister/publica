"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""

email = input("Enter your email: ").split("@")
username = email[0]
dom = email[1].split(".")
domain = dom[0]
col1 = 10
col2 = 15
print("--" * 20)
print(f"Username\t | \tDomaint")
print("--" * 20)
print(f"{username}\t | \t{domain}")