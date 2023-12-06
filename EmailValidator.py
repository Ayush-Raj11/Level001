############# PROGRAM TO CHECK THE VALIDITY OF AN EMAIL ############

import re
def check_valid(email):
    # Define a regular expression for a basic email validation by using literals
    email_format = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use the re.match() function to check if the email match with  the  above pattern of possible format.
    if re.match(email_format,email):
        return True
    else:
        return False
    
email_to_check = input("enter an email : ")
if check_valid(email_to_check):
    print(f"{email_to_check} is a valid email address.")
else:
    print(f"{email_to_check} is not a valid email address.")


