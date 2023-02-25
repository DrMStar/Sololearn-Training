"""
New Driver's License
You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

Task 
Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

Input Format 
Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

Output Format 
You will output an integer of the number of minutes that it will take to get your license.

Sample Input
'Eric'
2
'Adam Caroline Rebecca Frank'

Sample Output 
40
"""

name = input()
acount = int(input()) #agent count
others = input().split() 


#name = 'Eric'
#acount = 2
#others = 'Adam Caroline Rebecca Frank'.split()

others.append(name) #adding name to the list
sorted = sorted(others) #sorting list acc.2 alphabet
order = (sorted.index(name)) + 1 #getiing an order of the name in the list + 1, because list starts with 0

#counting of how many people can be served in 20 min. block
minutes = ((order // acount) * 20) 

#the cast when the name did not get into previous block
if order % acount > 0:
    minutes = minutes + 20

print(minutes)










