"""
Super Sale

Your favorite store is having a sale! You pay full price for the most expensive item that you get, but then you get 30% off of everything else in your purchase! How much are you going to save? 
Sales tax is 7%. 
Also, you leave anything below a dollar in your saving as a tip to the seller. If your saving is a round amount, you don't leave any tips.

Task: 
Given the prices of items you want to purchase, determine how much you will save during your shopping! 

Input Format: 
An string of numbers separated by commas that represent the prices for all of the items that you want to purchase (without tax).

Output Format: 
An integer number that represents the total savings that you got for shopping during the sale.

Sample Input: 
100.25,80.99,40.00

Sample Output: 
38

Explanation: 
With the sale, you would get 30% off of the second two items. The amount you save is $36.297, and $38.83779 when you consider the 7% tax. After leaving the 0.83779 as a tip, your final saving is $38.
"""
import math

prices = {0.0,} #set for parsed prises
tmp = "" #temp. var. for parsing
max = 0 #the highest price
rest = 0 # a sum of other prices
sale = 0 #how much I saved

vstup = input()
#vstup = "100.25,80.99,40.00"  #output: 38

#parsing of the input string
for i in vstup:
    if i != ",":
        tmp = tmp + i
    else:
        prices.add(float(tmp))
        tmp = ""
        
prices.add(float(tmp)) #last price adding from tmp
#print(prices)

#searching for the highest price
for j in prices:
    if j > max:
        max = j
        
#print(max)
    
#calculating of the rest of prices
for k in prices:
    if k != max:
        rest = rest + k

#print(rest)

#calculation of the sale
sale = math.floor(1.07 * ((max + rest) - (0.7 * (rest) + max)))

print(sale)

















