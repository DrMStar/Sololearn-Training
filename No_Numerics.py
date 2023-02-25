"""
You write a phrase and include a lot of number characters (0-9), but you decide that for numbers 10 and under you would rather write the word out instead. Can you go in and edit your phrase to write out the name of each number instead of using the numeral? 

Task: 
Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer.

Input Format: 
A string of the phrase in its original form (lowercase).

Output Format: 
A string of the updated phrase that has changed the numerals to words.

Sample Input: 
i need 2 pumpkins and 3 apples

Sample Output: 
i need two pumpkins and three apples
"""

vstup = input()
vystup = ""
cnt = 0
nutext = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "10" : "ten"
    }


for i in vstup:

    #checking if it is number
    if i.isnumeric():
    #checking 10    
        if i == "1":
            if vstup[cnt + 1] == "0":
                vystup = vystup + nutext["10"] 
            else: 
                vystup = vystup + nutext[i]
    #checking 0
        elif i == "0":
            if vstup[cnt - 1] == "1":
                vystup = vystup
            else: 
                vystup = vystup + nutext[i]
     #other numbers          
        else:
            vystup = vystup + nutext[i] 
       
    #it is not a number
    else:
        vystup = vystup + i
        
    cnt = cnt + 1
        
        
print(vystup)
    
