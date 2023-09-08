import re

def is_valid_password(password):
   
    if len(password) < 5:
        return False

    
    if '&' not in password:
        return False

    
    if not any(char.isupper() for char in password):
        return False

   
    if not any(char.islower() for char in password):
        return False

    
    return True


password = input("Enter a password: ")


if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password does not meet the requirements.")