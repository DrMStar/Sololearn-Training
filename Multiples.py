"""
Multiples

You need to calculate the sum of all the multiples of 3 or 5 below a given number.

Task: 
Given an integer number, output the sum of all the multiples of 3 and 5 below that number. 
If a number is a multiple of both, 3 and 5, it should appear in the sum only once.

Input Format: 
An integer.

Output Format: 
An integer, representing the sum of all the multiples of 3 and 5 below the given input.

Sample Input: 
10

Sample Output:
23

Explanation: 
The numbers below 10 that are multiples of 3 or 5 are 3, 5, 6 and 9.
The sum of these numbers is 3+5+6+9=23

"""

limit = int(input())
#limit = 9 #23
#limit = 100 #2318

a = 0
b = 0
num = {0,}
sum = 0

while a < limit:
    a = a + 3
    if (a < limit):
        num.add(a)

while b < limit:
    b = b + 5
    if (b < limit) and (b not in num):
        num.add(b)
        
for i in num:
    sum = sum + i
    
#print(num)    
print(sum)
    

















