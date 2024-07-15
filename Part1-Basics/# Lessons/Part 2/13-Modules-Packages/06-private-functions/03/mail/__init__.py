from .email import *

# By doing this, the mail package exposes only the send() function specified in the email.__all__ variable. It hides the attach_file() from the outside.
__all__ = email.__all__
