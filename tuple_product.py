#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#30 April 2021

"""
Write a Python program calculate the product, multiplying all the numbers of a given tuple.
"""

my_tuple = (1, 2, 3, 4, 5) #tuple of integers
my_list = list(my_tuple) #create a list from tuple items

product = 1 #initialize product to 1
for x in my_list:
    product = x * product

print(f"The product of {my_tuple}: ", product)