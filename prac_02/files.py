# Writes name into name.txt
out_file = open("name.txt", 'w')
name = input("Please enter your name: ")
print("{}".format(name), file=out_file)
out_file.close()

# Opens name.txt, reads it and prints name
in_file = open("name.txt")
name = in_file.read().strip()
print("Your name is {}".format(name))
in_file.close()

# Reads numbers.txt and adds the numbers in the lines together
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
total = number1 + number2
print("Total for {} + {} is {}".format(number1, number2, total))
in_file.close()

# Adds all the numbers in the file line by line
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print("Total is {}.".format(total))
in_file.close()
