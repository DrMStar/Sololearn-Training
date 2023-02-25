"""
Mathematics

Find which math expression matches the answer that you are given, if you have an integer answer, and a list of math expressions.

Task: 
Test each math expression to find the first one that matches the answer that you are given.

Input Format: 
Two inputs: an integer and a space separated string of math expressions. The following operations need to be supported: addition +, subtraction -, multiplication *, division /. 
An expression can include multiple operations.

Output Format: 
A string that tells the index of the first math expression that matches. If there are no matches, output 'none'.

Sample Input: 
15
(2+100) (5*3) (14+1)

Sample Output: 
index 1
"""
result = int(input())
#result = 17
expr = input().split()
#expr = ["(5*20)", "(88+22)", "(6-2)"]


ast = ""
bst = ""
a = 0
b = 0
op = ""
res = 0
index = 0
found = 0
#print(expr)

#parsing a list
for i in expr:
    #parsing a expression
    for j in i:
        if j =="(" or j == ")" or j == " ":
            zzz = 0
            
        elif j.isnumeric():
            if op == "":
                ast = ast + j
            else:
                bst = bst + j
                
        else:
            op = j
            
    #print(ast)
    #print(bst)
    
        
    a = int(ast)
    b = int(bst)
    #print(op)
    
    if op == "+":
        res = a + b    
        #print(res)
        
    elif op == "-":
        res = a - b    
        #print(res)
        
    elif op == "*":
        res = a * b
        #print(res)    
    
    elif op == "/":
        res = a / b
        #print(res)  
    
    #print(result)
    #print(res)
    if result == res:
        print("index", index)
        found = 1
     
    res = 0
    a = 0
    b = 0
    ast = ""
    bst = ""
    op = ""
    index = index + 1
    
if found == 0:
    print("none") 
    
    
    
    
    











