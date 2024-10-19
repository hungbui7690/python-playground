"""
Private

    is_valid_method = getattr(self, f'_{rule}')

"""

# Note that you can hide the required() and email() method by making them private. In this case, you also need to pass the rule prefixed with an underscore (_) to the getattr() function get the corresponding method:
import re


class Validation:
    ERRORS = {
        "required": "The {} is required",
        "email": "The {} is not a valid email address",
    }

    def _required(self, value):
        return len(value) > 0

    def _email(self, value):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.fullmatch(pattern, value)

    def validate(self, data, rules):
        errors = {}
        for field, rule in rules.items():
            is_valid_method = getattr(self, f"_{rule}")
            if not is_valid_method(data[field]):
                errors[field] = self.ERRORS[rule].format(field)

        return errors
