#Ques.1  Add all the digits of number 
n=input("Enter digits of number you want to add: ")
def getSum(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum
print(getSum(n))


num=int(input("Enter a number: "))
result=0
hold=num
while num>0:
    rem=num%10
    result=result+rem
    num=int(num/10)
print("Sum of all digits ",hold," is : ",result)