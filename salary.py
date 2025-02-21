list = []
action = "yes"
totalsavings = 0
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

    monthdic = {
        "month" : newMonth,
        "salary" : salary,
        "savings" : savings,
        "rent" : rent, 
        "electricity" : electricity,
        "total" : total,
        "remainingsalary" : remainingsalary,
        "estimatedyearlycost" : estimatedyearlycost,
        "totalsalarysquared" : totalsalarysquared,
           }

    list.append(monthdic)
    action = input("Enter yes to continue: ")

for i in range (len(list)):
        print(f"The month you entered is: {list[i]['month']}")
        print(f"The salary for  this month is: {list[i]['salary']}")
        print(f"The saving for  this month is: {list[i]['savings']}")
        print(f"The rent for  this month is: {list[i]['rent']}")
        print(f"The remainingsalary for  this month is: {list[i]['remainingsalary']}")
        print(f"The estimatedyearlycost for  this month is: {list[i]['estimatedyearlycost']}")
        print(f"The totalsalarysquared for  this month is: {list[i]['totalsalarysquared']}")

comp = input("Do you want to add additional amout: answer by yes or no: ")
if comp == "yes":
        additionalamount = float(input("Enter the additional amount:" ))
        addamountmonthly = 12 * additionalamount
        for i in range(len(list)):
                totalsavings += list[i]["savings"]
               
        leftamount = addamountmonthly / totalsavings

print(f"The totalsavings amount is: {totalsavings} and the left amount is: {totalsavings} ")
