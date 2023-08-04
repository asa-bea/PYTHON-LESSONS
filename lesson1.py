
#EXAMPLE 1
# Ask the user to input their name and assign it to a variable named name

name = input("What is your name ")

# Print out hello followed by the name printed

print("Hello", name)

 # ask user to input two values, num1 and num2
num1, num2 = input('Enter two numbers ').split()

 # convert strings into int
num1 = int(num1)
num2 = int(num2)

 # add the values and store in variable named sum  
sum = num1 + num2

 # multiply the values and store in variable named product 
product = num1 * num2
 
 # subtract the values and store in variable named difference
difference = num1 - num2
 
 # divide the values and store in variable named quotient
quotient = num1 / num2

 # use modulos on the values to find the remainder
remainder = num1 % num2

 # print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} * {} = {}".format(num1, num2, product))
print("{} - {} = {}".format(num1, num2, difference))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder)) 



# EXAMPLE 2
# User receives miles and converts to kilometer
# kilometers = miles * 1.60934
# Enter Miles 5

miles = input('Enter distance in miles')
miles = float(miles)
kilometers = miles * 1.60934
kilometers = float(kilometers)

print('Value of {}miles in kilomteres is {}'.format(miles, kilometers))




#EXAMPLE 3
# basic calculator operation
num1, operator, num2 = input("enter calculation ").split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
    print("{} * {} = {}".format(num1, num2, num1*num2))
else:
    print('This program only adds, subtract, multiplies and divides')





   # EXAMPLE 4
# Provide output based on age
# 1 - 18 -> important
# 21, 50, >65 -> important
# all other birthdays  -> not important

age = eval(input("Enter age :"))
if (age >= 1) and (age <= 18):
    print("Important Birthday")

elif(age == 21) or (age == 50):
    print("Important Birthday")

elif not(age < 65):
    print("Important Birthday")

else:
    print("Sorry, not important birthday")

   

 #EXAMPLE 5
#if age is 5 go to kindergarten
#ages 6 through 17 goes to grades t through 12
#ages greater than 17 goes to college

age = eval(input("what is your age: "))
if age < 5:
    print("too young for school")
elif age == 5:
    print("Go to kindergarten")
elif (age >= 6) and (age <= 12):
    print("Go to grades 1 through 12")
else:
    print("goes to college")
