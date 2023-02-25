#vstup = "zkusebni text k prekladu"
vstup = input()
vystup = "" #output
prvni = "" #first letter of a word in text
telo = "" #a rest of body of the word
index = 1 #a flag, if the first letter is read

for i in vstup:
    if index == 1: #saving of tthe first letter
        prvni = i
        index += 1
        
    elif i != " ": #collecting of a rest of body
        telo = telo + i
        
    else: 
        #composing of the output
        vystup = vystup + telo + prvni + "ay" + " "
        #reseting of variables for new word
        index = 1
        prvni = ""
        telo = ""

#adding of last word of the text
vystup = vystup + telo + prvni + "ay" 

print(vystup)
