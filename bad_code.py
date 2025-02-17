num1= input("Enter a number: ")
num2 = input("Enter another number: ")
def addition(num1, num2):
    #verifying input type
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        #intializing sum variable
        sum=0
        #adding first number to sum
        sum=sum+num1
        #adding second number to sum
        sum=sum+num2
        return sum
    else:
        return "invalid input"

#Avery-Subtraction-Documentation

#Yana-Multiplication-Dry

#Bita-Divison-CleanCode