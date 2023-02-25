"""
You and three friends go to a baseball game and you offer to go to the concession stand for everyone. They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.

Task 
Determine the total cost of ordering four items from the concession stand. If one of your friend’s orders something that isn't on the menu, you will order a Coke for them instead.

Input Format
You are given a string of the four items that you've been asked to order that are separated by spaces.

Output Format 
You will output a number of the total cost of the food and drinks.

Sample Input 
'Pizza Cheeseburger Water Popcorn'

Sample Output 
26.75
"""

vstup = input()
#vstup = "Pizza Cheeseburger Water Popcorn"
menu = {
    "Pizza" : 6.0,
    "Nachos" : 6.0,
    "Cheeseburger" : 10.0,
    "Water" : 4.0, 
    "Coke" : 5.00
}
item = ""
price = 0

"""

#adding a space to easier parsing of last item
vstup = vstup + " "

for i in vstup:
    if i != " ":
        item = item + i
    else:
        if item in menu:
            price = price + menu[item]
        else:
            if item != "":
                price = price + menu["Coke"]
            
        item = ""      
        
"""

item = vstup.split()

for i in item:
    if i in menu:
        price = price + menu[i]
    else:
        price = price + menu["Coke"]
    

price = price * 1.07 #tax

"""

#price = round(price, 2) 
price = price * 100
zbytek = price % 1
if zbytek < 0.5:
    price = (price // 1)/100
else:
    price = ((price // 1) + 1)/100

            
print(price)
"""
print("{:.2f}".format(round(price,2)))

