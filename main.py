import Class_Definitions as cd
import pandas as pd

print("Welcome")
count = 'y'
while count == 'y':
    prod1=cd.product(name=input("Enter Product name : "), price=int(input("Enter the price : ")), quantity=int(input("Enter the quantity : ")))
