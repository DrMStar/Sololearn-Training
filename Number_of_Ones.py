"""
Number of Ones

Task:
Count the number of ones in the binary representation of a given integer.

Input Format:
An integer.

Output Format: 
An integer representing the count of ones in the binary representation of the input.

Sample Input:
9

Sample Output:
2

Explanation: 
The binary representation of 9 is 1001, which includes 2 ones.

"""
vstup = str(bin(int(input())))
ones = 0

#print(vstup)

for i in vstup:
    if i == "1":
        ones = ones + 1
        
print(ones)



















