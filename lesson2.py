'''
# EXAMPLE 1
# print a list of odd numbers from 1 to 20
# use a for loop, modulo and range

for i in range(1, 21):
    if((i % 2) != 0):
        print("The odd numbers: ", i)

# EXAMPLE 2
# working with floats

your_float = input("Enter a float ")
your_float = float(your_float)
print("round to 2 decimals : {:.2f}".format(your_float))

 

# EXAMPLE 3

# compunding interest
# have the user enter their invested amount and expected interest
# each year their investment increases by their investment + investment * rate
# print out earnings after 10 years period

investment = input("Enter your investment: ")
rate = input("Enter rate: ")

investment = float(investment)
rate = float(rate) * .01

compounded_interest = investment + (investment * rate) * 120
print("Your interest over 10 years is ", compounded_interest)



# EXAMPLE 4 - WHILE LOOP

import random

random_num = random.randrange(1,51)

i = 1
while (i != random_num):
    i += 1
    print(" the random value is ", random_num)

'''

# EXAMPLE 5
# prints out a pine tree

tree_height = input("How tall is the tree: ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
Stump_spaces = tree_height - 1

while tree_height > 0:

    for i in range(spaces):
        print(' ', end="")

    for i in range(hashes):
        print('#', end="")    

    print()

    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(Stump_spaces):
        print(' ', end="")
print("#")