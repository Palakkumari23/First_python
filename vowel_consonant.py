string=input("enter n:")
vowel="aeiouAEIOU"
count=0

for char in string :
    if char in vowel:
        count+=1
        
        
print("number of vowels",count)