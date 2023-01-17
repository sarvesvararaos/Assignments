
#1st Answer
x=[10,20,30,40,10]
y=[75,64,75,24]
def isListSameOrNot(nums):
    return bool(nums[0]==nums[-1])

print(isListSameOrNot(x))
print(isListSameOrNot(y))

#2nd Ans
x=[10,15,20,21,23]
num = list(filter(lambda t:t%5==0,x))
print(num)

#3rd answer
str_x="emma is good girl.emma age is 19"
print("emaa name count: ",str_x.count("emma"))

#4th ans
palin = 545
temp = palin  
rev = 0  
while(palin > 0):  
    dig = palin % 10  
    rev = rev * 10 + dig  
    palin = palin // 10  
if(temp == rev):  
    print("Yes, givem value is a palindrome number")  
else:  
    print("No, givem value is not a palindrome number")  


palin = 5456
temp = palin  
rev = 0  
while(palin > 0):  
    dig = palin % 10  
    rev = rev * 10 + dig  
    palin = palin // 10  
if(temp == rev):  
    print("Yes, givem value is a palindrome number")  
else:  
    print("No, givem value is not a palindrome number")  

#5th ans
num= 5634
while num>0:
    digit=num%10
    num= num//10
    print(digit,end=' ')
