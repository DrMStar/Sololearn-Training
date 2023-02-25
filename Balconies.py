"""
Balconies
You are trying to determine which of two apartments has a larger balcony. Both balconies are rectangles, and you have the length and width, but you need the area.

Task 
Evaluate the area of two different balconies and determine which one is bigger.

Input Format 
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.

Output Format: 
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input 
'5,5'
'2,10'

Sample Output 
Apartment A
"""

#-------------------------------------
class Balcony:
    def __init__(self, text):
       
#separating w and l where sep is an indicator of coma was detected
        w =""
        l = ""
        sep = 0
        for i in text:
            if i.isnumeric():
                if sep == 0:
                    w = w + i
                else:
                    l = l + i
            else:
                sep = 1
        #calculation of area    
        self.area = int(w) * int(l)
   
#comparing of areas of two variables of class Balcony
    def __gt__(self, other):
        if self.area > other.area:
            return "Apartment A"
        else:
            return "Apartment B"
        
#-------------------------------------

apa = Balcony(input())
apb = Balcony(input())

#apa = Balcony("5, 5")
#apb = Balcony("2, 10")

#print(apa.area)
#print(apb.area)

print(apa > apb)




        
