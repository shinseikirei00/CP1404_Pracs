# get user to input 5 numbers and save it into list called numbers
numbers = []
number_of_inputs = 5

for i in range(0, 5, 1):
    user_input = int(input("Number: "))
    numbers.append(user_input)


print("The first number is {}\n".format(numbers[0]))
print("The last number is {}\n".format(numbers[-1]))
print("The smallest number is {}\n".format(min(numbers)))
print("The largest number is {}\n".format(max(numbers)))
print("The average of the numbers is {}\n".format(sum(numbers)/5))
