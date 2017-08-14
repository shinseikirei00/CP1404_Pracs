print("Electricity Bill Estimator ver. 1.0")

price = float(input("Please enter price of kWh in cents: "))
power_used = float(input("Please enter daily use in kWh: "))
billing_days = int(input("Please enter total amount of billing days: "))

total_bill = (billing_days * power_used) * price

print("Estimated bill: ${:.2f}".format(total_bill))
