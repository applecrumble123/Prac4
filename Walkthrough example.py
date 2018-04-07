"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
def add_Values(mylist):
    #mylist = incomes
    total = 0
    month = 0
    print("\nIncome Report\n-------------")
    for income in mylist:
        #reading the income in the list
        total += income
        #accumulating the income
        month +=1
        #accumulating the month

        print("Month {} - Income: ${} Total: ${}".format(month,income,total))

def input_Values():
    monthly_income = []
    #make monthly_income an empty list(making it a list)
    num_of_month = int(input("How many months? "))
    #input the number of months

    for month in range(1, num_of_month + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        #capture input from the keyboard
        monthly_income.append(income)
        #add on into the list for income
    return monthly_income
    #send back to the list to the main

"""Display income report for incomes over a given number of months."""

incomes = input_Values()
print(incomes)
#create the list and input value inside

add_Values(incomes)
#passing the list to the function, calculate the total and diaplay the list




