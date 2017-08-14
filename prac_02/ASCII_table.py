# # ASCII Table
# # by: Jan Crooks

LOWER = 33
UPPER = 127

ascii_character = input("Please enter a character: ")
print("The ASCII code for {} is {}".format(ascii_character, ord(ascii_character)))

ascii_number = int(input("Please enter a number between {} and {}: ".format(LOWER, UPPER)))
while ascii_number < LOWER or ascii_number > UPPER:
    ascii_number = int(input("Please input a valid number between {} and {}: ".format(UPPER, LOWER)))
print("The character for {} is {}".format(ascii_number, chr(ascii_number)))

# ASCII Table
for value in range(LOWER, UPPER + 1):
    print("{:3} {:>4}".format(value, chr(value)))
