# 1. Python Program to find the area of a circle using radius.
from math import *
# def findArea(r):
#     # PI = 3.142
#     # return PI * (r*r)
#     return pi*r*r
# x=int(input("Enter radius of circle: \n"))
# print("Area is %.2f" %findArea(x))

# 2. Write a Python Program for Sum of squares of first n natural numbers

# Input : N = 5 
# Output : 55 ----> (1+4+9+16+25)

# def squaresum(a):
#     sm = 0
#     for i in range(1, n+1) : 
#         sm = sm + (i * i)
#     return sm
# n = int(input("Enter a number: "))
# print(squaresum(n))

# 3.Write a Python program to interchange first and last elements in a list.

# Input : [32, 75, 29, 51, 84]
# Output : [84, 75, 29, 51, 32]

# def swapList(newList): 
#     n= len(newList) 
#     temp = newList[0] 
#     newList[0] = newList[n - 1] 
#     newList[n - 1] = temp 
#     return newList 
# lst=[]
# no= int(input("Enter the number of elements in list:"))
# for x in range(0,no):
#     element=int(input("Enter element " + str(x+1) + ":"))
#     lst.append(element)
# print("Original list is:\n "+str(lst))
# print("New list is:\n "+str(swapList(lst))) 

# 4. Write a Python program to find smallest number in a list.

# Input : list1 = [10, 20, 4]
# Output : 4

# list1 = [18, 26, 14, 5, 9]
# list1.sort()
# # print("Smallest element is:",*list1[:1])
# print("Smallest number is: "+str(list1[0]))

# 5. Write a Python program to print even numbers in a list.
# Input: list1 = [24, 71, 15, 68, 14] 
# Output: [24, 68, 14]

# list1=[]
# no= int(input("Enter the number of elements in list:"))
# for x in range(0,no):
#     element=int(input("Enter element " + str(x+1) + ":"))
#     list1.append(element)
# for num in list1:  
#     if num % 2 == 0: 
#         print(num, end = " ")

# 6.Write a Python program to print all negative numbers in a range.

# Input: start = -4, end = 5
# Output: -4, -3, -2, -1

# start, end = -6, 15
# for num in range(start, end + 1): 
#     if num < 0: 
#         print(num, end = " ") 

# 7. Python program to check if a string is palindrome or not.

# Input : mom Output : Yes
# Input : geeks Output : No

# def isPalindrome(s): 
#     return s == s[::-1] 
# s = input("Enter a string:\n")
# ans = isPalindrome(s) 
# if ans: 
#     print("Yes, it is a palindrome") 
# else: 
#     print("No, it is not a palindrome")

# 8.Python program to print even length words in a string.

# Input: s = "I am Anjana"
# Output: am
#         Anjana

# def printWords(s):
#     s = s.split(' ')
#     for word in s:
#         if len(word)%2==0:
#             print(word)
# string1 = input("Enter a string:\n")
# printWords(string1)

# 9. Write a Python program to convert time from 12 hour to 24 hour format. 

# Note : Midnight is 12:00:00 AM on a 12-hour clock and 00:00:00 on a 24-hour clock. 
# Noon is 12:00:00 PM on 12-hour clock and 12:00:00 on 24-hour clock. 
# Input : 11:21:30 PM 
# Output : 23:21:30 
# Input : 12:12:20 AM Output : 00:12:20

# def convert24(str1):
#     if str1[-2:] == "AM" and str1[:2] == "12":
#         return "00" + str1[2:-2]
#     elif str1[-2:] == "PM" and str1[:2] == "12":
#         return str1[:-2]
#     elif str1[-2:] == "AM":
#         return str1[:-2]
#     else:
#         return str(int(str1[:2]) + 12) + str1[2:8]
# n=input("Enter time in 00:00:00 AM\PM format: \n")
# print(convert24(n))

# 10. Write a Python Program for n-th Fibonacci number.
# Fn = Fn-1 + Fn-2
# F0 = 0 and F1 = 1.

# def Fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     elif n==1: 
#         return 0 
#     elif n==2: 
#         return 1
#     else: 
#         return Fibonacci(n-1)+Fibonacci(n-2)
# no=int(input("Enter a no: \n"))
# print(Fibonacci(no))