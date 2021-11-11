import re
#check whether the string starts with "The" and ends with "you"
# txt="How are you"
# x=re.search("^How.*you$",txt)
# x=re.search("^How",txt)
# x=re.search("you$",txt)
# if x:
#     print("Yes! there's a match...")
# else:
#     print("No match!")

#findall ---> returns list of contents found
# print(re.findall("ow",txt))
# print(re.search("ow",txt))

#search  ---> returns index(span) of contents found
# txt = "hello world"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start()+1)

# txt = "Good Morning everyone"
# x = re.split("\s", txt, 1)
# print(x)

#replace
# txt = "Hello everyone there "
# # x = re.sub("\s", "_", txt)
# x = re.sub("\s", "_", txt, 1)
# print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())


 
    
