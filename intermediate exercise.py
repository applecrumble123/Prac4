def inputvalues():
    """Input 5 values"""
    numbers = []
    #make the number into a list
    for number in range (5):
        value = int(input("Enter a number: "))
        numbers.append(value)
        #add on the number
    return numbers

def calculateAverage(mylist):
    #the parameter has to be different so it will not be confusing
    sum = 0
    for number in range(len(mylist)+1):
    #+1 to add in the last element
        sum = sum + number
    return sum / len(mylist)
#calculate the average and return it



number_list = inputvalues()


print("\n")
print("The first number is : ", number_list[0])
print("The last number is : ", number_list[len(number_list)-1])
print("The smallest number is: ", min(number_list))
print("The largest number is: ", max(number_list))
print("The average of the numbers : ", calculateAverage(number_list))
#calling the function and make the own function your own for number_list




