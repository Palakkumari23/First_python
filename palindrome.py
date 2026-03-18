num=int(input("enter n:"))
original_number=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse * 10 + digit
    num=num//10
    
    
if original_number == reverse:
    print("palindrome number")
else:
    print("not a palindrom")