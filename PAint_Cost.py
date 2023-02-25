"""
You are getting ready to paint a piece of art. The canvas and brushes that you want to use will cost 40.00. Each color of paint that you buy is an additional 5.00. Determine how much money you will need based on the number of colors that you want to buy if tax at this store is 10%.

Task 
Given the total number of colors of paint that you need, calculate and output the total cost of your project rounded up to the nearest whole number.

Input Format 
An integer that represents the number of colors that you want to purchase for your project.

Output Format 
A number that represents the cost of your purchase rounded up to the nearest whole number.

Sample Input 
10

Sample Output 
99
"""

import math

colors = int(input())

#(canvas and brushes + 5 * colors) + 10 %
cost = (40 + 5 * colors) * 1.1


"""
I do not know why, but result of (40 + 5 * 2)*1.1 is not exactly 55, so I added one more step with rounding to make the code pass. It is piddy solution, but it works
"""

cost = round(cost, 3)

#roundig to a higher number
if cost % 1 != 0:
    cost = (cost // 1) + 1
else:
    cost = cost // 1
    
# other possibility of rounding 
# cost = math.ceil(cost)
    
print(int(cost))

