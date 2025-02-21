list = []
action = "yes"

while action == "yes":
    salary = float(input("Please enter your salary: "))
    newMonth = input("Enter the month you are storing the salary for: ")
    savingspercentage = float(input("Enter the percentage of savings: "))
    rentpercentage = float(input("Enter the percentage of rent: "))
    electricitypercentage = float(input("Enter the percentage of electricity: "))

    savings = salary * savingspercentage / 100.0
