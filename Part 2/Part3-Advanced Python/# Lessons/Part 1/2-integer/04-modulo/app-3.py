"""
Practical Python modulo operator


"""


# 2) Using the modulo operator to convert units
# The following example uses the modulo operator (%) to convert seconds to days, hours, minutes, and seconds. It can be handy if you want to develop a countdown program:

from math import floor


def get_time(total_seconds):
    return {
        "days": floor(total_seconds / 60 / 60 / 24),
        "hours": floor(total_seconds / 60 / 60) % 24,
        "minutes": floor(total_seconds / 60) % 60,
        "seconds": total_seconds % 60,
    }


print(get_time(93750))  # {'days': 1, 'hours': 2, 'minutes': 2, 'seconds': 30}


# Summary
# Python uses the percent sign (%) as the modulo operator.
# The modulo operator (%) always satisfies the equation N = D * ( N // D) + (N % D).
