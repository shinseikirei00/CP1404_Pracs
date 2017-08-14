error_check = True
price = 0.00

option = int(input("Which tariff? 11 or 31: "))
while error_check == True:

    if option == 11:
        price = 0.244618
        error_check = False

    elif option == 31:
        price = 0.136928
        error_check = False

    else:
        option = input("Please enter a valid tariff. 11 or 31: ")

daily_use = int(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))

total_price = (daily_use*days) * price

print("Estimated bill: ${:.2f}".format(total_price))
