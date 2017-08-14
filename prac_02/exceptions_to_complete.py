"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0

while not finished:
    try:
        # TODO: this line
        # TODO: this line
        result = int(input("Please enter an integer: "))
        finished = True
        #Pass

    except ValueError:
        # TODO - add something after except
        print("Not a valid Integer Number")


print("Valid result is:", result)
