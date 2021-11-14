# 11) Write a Python Program to Check if a Number is an Armstrong Number?

# 0, 1, 153, 370, 371 and 407 are an Armstrong number list or all examples of Armstrong numbers. 
#  For 0, the operation is 0^1=0
#  For 1, the operation is 1^1=1
#  For 153, the operation is 1^3 5^3 3^3=153
#  For 370 the operation is 3^3 7^3 0^3=370
#  For 371 the operation is 3^3 7^3 1^3=371
#  For 407 the operation is 4^3 0^3 7^3=407

# n=int(input("Enter any number: "))
# a=list(map(int,str(n)))
# b=list(map(lambda x:x**3,a))
# if(sum(b)==n):
#     print("The number is an armstrong number. ")
# else:
#     print("The number isn't an arsmtrong number. ")

# 12) Write a Python Program to Check if a Number is a Perfect Number?

# Eg. The proper factors of 28 are 1,2,4,7 and 14.The sum of proper factors is 28. 
# According to the definition of perfect numbers, 28 is a perfect number.

# n = int(input("Enter any number: "))
# sum1 = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum1 = sum1 + i
# if (sum1 == n):
#     print("The number is a Perfect number!")
# else:
#     print("The number is not a Perfect number!")

# 13) Write a Python Program to Check if a Number is a Strong Number?

# If the sum of factorial of each digit is equal to the given number then the given number is strong otherwise not. 
# Eg.- The given number is 145, we have to pick each digit and find the factorial 1! = 1, 4! = 24, and 5! = 120. 
# Now, we will do the sum of the factorials, we get 1+24+120 = 145, which is exactly the same as the given number.

# sum1=0
# num=int(input("Enter a number:"))
# temp=num
# while(num):
#     i=1
#     f=1
#     r=num%10
#     while(i<=r):
#         f=f*i
#         i=i+1
#     sum1=sum1+f
#     num=num//10
# if(sum1==temp):
#     print("The number is a strong number")
# else:
#     print("The number is not a strong number")

# 14) Write a Python Program to Find the Second Largest Number in a List?

# a=[]
# n=int(input("Enter number of elements:"))
# for i in range(1,n+1):
#     b=int(input("Enter element:"))
#     a.append(b)
# a.sort()
# print("Second largest element is:",a[n-2])

# 15) Write a Python Program to Swap the First and Last Value of a List?

# a=[]
# n= int(input("Enter the number of elements in list:"))
# for x in range(0,n):
#     element=int(input("Enter element " + str(x+1) + ":"))
#     a.append(element)
# temp=a[0]
# a[0]=a[n-1]
# a[n-1]=temp
# print("New list is:")
# print(a)

# 16) Write a Python Program to Check if a String is a Palindrome or Not?

# string=input("Enter string:")
# if(string==string[::-1]):
#     print("The string is a palindrome")
# else:
#     print("The string isn't a palindrome")

# 17) Write a Python Program to Count the Number of Vowels in a String.

# string=input("Enter string:")
# vowels=0
# for i in string:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#         vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)

# 18) Write a Python Program to Check Common Letters in Two Input Strings?

s1=input("Enter the first string:")
s2=input("Enter the second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)

# 19) To print sum of unknown list/tuples of no
# def goals(*a): return sum(a)
# print(goals(2,3,4))
