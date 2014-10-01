"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
"""

# create variable to count the number of vowels
numVowels = 0

# iterate through the characters in string s
for char in s:
    
    # if that character from string s is a vowel, increase numVowels by 1
    if char in 'aeiouAEIOU':
        numVowels +=1
        
    # if that character is not a vowel, do not increase numVowels
    else:
        numVowels +=0

# print the final value of numVowels
print('numVowels is: ' + str(numVowels))


"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
"""

# create variable to count the number of bobs
numBob = 0

# find the length of string s
length = int(len(s))

# set the lower and upper bounds
x = 0
y = 3

# execute this as long as the upper bound (y) does not exceed the length of the string s
while y <= length:
    
    # set variable z equal to the section of string s from the lower to upper bound
    z = s[x:y]
    
    # if z is bob, increase numBob by 1
    if z == 'bob':
        numBob += 1
    
    # if z is not bob, do not increase numBob
    else:
        numBob += 0
    
    # increase the lower and upper bounds by 1 and repeat
    x += 1
    y += 1

# print the final value of numBob
print('Number of times bob occurs is: ' + str(numBob))