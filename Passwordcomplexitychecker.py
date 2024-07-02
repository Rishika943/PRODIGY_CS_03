import re

def validate_password(password):
    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    # If all the conditions are met, the password is valid
    return True

password = input("Input your password: ")
is_valid = validate_password(password)

if is_valid:
    print("Valid Password.")
else:
    print("Password does not meet requirements.")
