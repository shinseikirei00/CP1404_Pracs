# """
# CP1404/CP5632 - Practical
# Broken program to determine score status
# """
#
# # TODO: Fix this! # Done!
#
# score = int(input("Enter score: "))
#
# # if score < 0:
# #     print("Invalid score")
# # else:
# #     if score > 100:
# #         print("Invalid score")
# #     if score > 50:
# #         print("Passable")
# #     if score > 90:
# #     print("Excellent")
# # if score < 50:
# #     print("Bad")
#
# if score < 0 or score > 100:
#     print("Invalid Score")
#
# elif score >= 90:
#     print("Excellent")
#
# elif score >= 50:
#     print("Passable")
#
# else:
#     print("Bad")
#
def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
