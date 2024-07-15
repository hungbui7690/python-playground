"""
try…except…else

    try:
        # code that may cause errors
    except:
        # code that handle exceptions
    else:
        # code that executes when no exception occurs


- The try...except...else statement works as follows:

    If an exception occurs in the try clause, Python skips the rest of the statements in the try clause and the except statement execute.
    In case no exception occurs in the try clause, the else clause will execute.

- When you include the finally clause, the else clause executes after the try clause and before the finally clause.

"""


# 1) Using try…except…else statement for control flow

# The following example illustrates how to use the try...except...else clause develop a program that calculates the body mass index (BMI).
# First, define a function for calculating the (BMI) based on height and weight:


def calculate_bmi(height, weight):
    """calculate body mass index (BMI)"""
    return weight / height**2


# Second, define another function for evaluating BMI:


def evaluate_bmi(bmi):
    """evaluate the bmi"""
    if 18.5 <= bmi <= 24.9:
        return "healthy"

    if bmi >= 25:
        return "overweight"

    return "underweight"


# Third, define a new main() function that prompts users for entering height and weight, and prints out the BMI result:


def main():
    try:
        height = float(input("Enter your height (meters):"))
        weight = float(input("Enter your weight (kilograms):"))

    except ValueError as error:
        print("Error! please enter a valid number.", error)
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f"Your body mass index is {bmi}")
        print(f"This is considered {evaluation}!")


main()

# The main() function uses the try...except...else statement to control its flow. If you enter height and weight that cannot be converted to numbers, the ValueError exception will occur.

# If no exception occurs, the else clause will execute. It calculates the BMI index and displays the evaluation.
