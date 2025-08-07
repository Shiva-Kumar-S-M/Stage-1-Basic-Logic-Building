#Check if a passwprd is strong(has upper/lowercase ,number,special char)
import re

def is_password_strong(password):
    if len(password)<8:
        return print("Password should be at least 8 characters long.")
    if not re.search(r"[A-Z]",password):
        return print("Missing Uppercase letter.")
    if not re.search(r"[a-z]",password):
        return print("Missing LowerCase Letter.")
    if not re.search(r"[0-9]",password):
         return  print("Missing Number:")
    if not re.search(r"[!@#$%^&*()_]",password):
        return print("Missing special character")
    return print("Password is strong.")

password=input("Enter Your password:")
print(is_password_strong(password))

    