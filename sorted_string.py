"""Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz
"""
#code 1
def longest_str(a1, a2):
    return "".join(sorted(set(a1 + a2)))

#code 2
def longest(s1, s2): 
    set1 = set(s1) 
    set2 = set(s2) 
    return "".join(sorted(set1 | set2))

print(longest("abzjjb","fowdd"))
