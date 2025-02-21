list = []
action = "yes"

while action == "yes":
    salary = float(input("Please enter your salary: "))
    newMonth = input("Enter the month you are storing the salary for: ")
    savingspercentage = float(input("Enter the percentage of savings: "))
    rentpercentage = float(input("Enter the percentage of rent: "))
    electricitypercentage = float(input("Enter the percentage of electricity: "))

    savings = salary * savingspercentage / 100.0
    rent = salary * rentpercentage / 100.0
    electricity = salary * electricitypercentage / 100.0
    total = savings + rent + electricity
    remainingsalary = salary - total
    estimatedyearlycost = (rent + electricity) * 12
    totalsalarysquared = salary ** 2
