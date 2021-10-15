"""
Complete the function that accepts a string parameter, and reverses each word in the string.
 All spaces in the string should be retained.
Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""
def reverse_words(str):
    #print(''.join(str[::-1] ))
    return ' '.join(s[::-1] for s in str.split(' '))
str="Hello sonu"
print(reverse_words(str))
#print(str.split(' '))