"""
Gotcha
- As mentioned in the module tutorial, the import * is not a good practice and often leads to bugs. However, you still can utilize it by using a package.

"""

# 1. First, create a package called mail with the __init__.py file and create the email.py module in the mail package

# 2. mail/email.py

# 3. Third, use the import * and add the send() function to the __all__ variable in the __init__.py:

# 4. From the main.py file, you can import the mail package and use the send() function like this:
# Method 1
# import mail
# mail.send("test@example.com", "Hello")

# Method 2
from mail import send

send("test@example.com", "Hello")  # Method 2
