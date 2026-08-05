#reverse a string
a = "hello world \n this is my first string program"
print(a[::-1])

#--------------------------------------------------------------------------------------
#check vowels and consonants
vowels = "aeiouAEIOU"
char = input("Enter a character : ")
if char.isalpha():
    if char in vowels:
        print("Its a vowel")
    else:
        print("its not a vowel but it is a consonant")
else:
    ("invalid character")

#---------------------------------------------------------------------------------------
#count characters
word = "supercalifragilisticexpialidocious"
count = 0
for i in word:
    count = count+1
print(count)

#----------------------------------------------------------------------------------------
#count words
sentence = "Python is easy to learn"
words = sentence.split()
print(len(words))

#---------------------------------------------------------------------------------------
#palindrome
num = 12321
original = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("It's a palindrome")
else:
    print("Not a palindrome")

#----------------------------------------------------------------------------------------
#remove all vowels from a string
user = input("Enter a sentence")
vowels = "aeiouAEIOU"
res = ""
for i in user:
    if i not in vowels:
        res += i
print(res)

#----------------------------------------------------------------------------------------
#anagram check
s1 = "race"
s2 = "care"
if sorted(s1) == sorted(s2):               #sorted()____returns list of characters,not a string
    print("its an anagram")
else:
    print("not an anagram")

#------------------------------------------------------------------------------------------
#print every second character
a = "hello world"
print(a[::2])

#------------------------------------------------------------------------------------------
#find first and last character
user = input("Enter any word or sentence : ")
print("first occurance : ",user[0])
print("last occurance : ",user[-1])

 
