"""
A practical example of the Python getattr() function
- In practice, you’ll use the getattr() function to call the method of an object dynamically. Note that a method is also an attribute of an object.

"""

import re

"""
Suppose, you need to validate the name and email with the following rules:

    name is required i.e., its length is greater than zero.
    email is a valid email address

To do that, you can create a reusable Validation class and use it as follows:
"""


# First, define a Validation class:
# Second, declare the error messages (ERRORS) for the required and email rules:
class Validation:
    ERRORS = {
        "required": "The {} is required",
        "email": "The {} is not a valid email address",
    }

    # Third, define the required() method that returns True if the length of a value is greater than zero and email() method that returns True if a value is a valid email address:
    def required(self, value):
        return len(value) > 0

    # To validate an email address, the email() method uses the fullmatch() function from the regular expression (re) module.
    def email(self, value):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.fullmatch(pattern, value)

    # Finally, define the validate() method:
    def validate(self, data, rules):
        errors = {}
        for field, rule in rules.items():
            is_valid_method = getattr(self, rule)
            if not is_valid_method(data[field]):
                errors[field] = self.ERRORS[rule].format(field)

        return errors


"""
In the validate() method:

    Initialize an errors dictionary to store error messages.
    Iterate the rules from the rules dictionary.
    For each rule, use the getattr() function to find the method that is corresponding to the rule. For example, the getattr() returns the required method for the required rule and email method for the email rule.
    Call the method dynamically to validate data. If the method returns False, add the error message to the errors dictionary.
    Return the errors.
"""

validation = Validation()
data = {"name": "", "email": "test"}
rules = {"name": "required", "email": "email"}
errors = validation.validate(data, rules)
print(errors)
# {'name': 'The name is required', 'email': 'The email is not a valid email address'}


# If you pass the valid data, the errors will be empty:
if __name__ == "__main__":
    validation = Validation()
    data = {"name": "John", "email": "john@pythontutorial.net"}
    rules = {"name": "required", "email": "email"}
    errors = validation.validate(data, rules)
    print(errors)  # {}
