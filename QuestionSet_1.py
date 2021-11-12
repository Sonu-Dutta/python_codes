#  1) What is the output of the program?
# n1 = ['Mango', 'Grapes', 'Orange', 'Apple']
# n2 = n1
# n3 = n1[:]

# n2[0] = 'Guava'
# n3[1] = 'Strawberry'

# sum = 0
# for ls in (n1, n2, n3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Strawberry':
#         sum += 10
# print(sum)

# A) 12

# 2) What is the output, Suppose list1 is [1, 3, 2], What is list1 * 2?

# A) [1, 3, 2, 1, 3, 2]

# 3) What is the output when we execute list(“hello”)?

# A) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]


# 4) Write a program to find the average of numbers in a list in Python?

# n=int(input("Enter the number of elements to be inserted: "))
# a=[]
# for i in range(0,n):
#     elements=int(input("Enter element: "))
#     a.append(elements)
# print(a)
# avg=sum(a)/n
# print("Average of elements in the list",round(avg,2))

# 5) Write a program to reverse a number.

# n=int(input("Enter number: "))
# rev=0
# while(n>0):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print("The reverse of the number:",rev)

# 6) Write a program to find the sum of the digits of a number.

# n=int(input("Enter a number:"))
# total=0
# while(n>0):
#     digit=n%10
#     total=total+digit
#     n=n//10
# print("The total sum of digits is:",total)

# 7) Write a Python Program to Check if a Number is a Palindrome or not?

# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# 8) Write a Python Program to Count the Number of Digits in a Number?

# n=int(input("Enter number:"))
# # method 1
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print("The number of digits in the number is:",count)

# method 2
# a=str(n)
# print("The number of digits in the number is:",len(a))



# 9) Write a Python Program to Print Table of a Given Number.

# n=int(input("Enter the number to print table :"))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)

# 10) Write a Python Program to Check if a Number is a Prime Number?

# method 1
# a=int(input("Enter number: "))
# k=0
# for i in range(2,a//2+1):
#     if(a%i==0):
#         k=k+1
# if(k<=0):
#     print("Number is prime")
# else:
#     print("Number is not prime")

# method 2

num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")