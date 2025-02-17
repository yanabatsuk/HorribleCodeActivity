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


# Variable for number 1
a = input("Enter a number: ")
# Variable for number 2
b = input("Enter another number: ")
# Function to complete math.
def m(a, b):
    # Return a - b
    return a - b

#Yana-Multiplication-Dry

#Bita-Divison-CleanCode