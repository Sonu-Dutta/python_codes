"""
ATM machines allow 4 or 6 digit PIN codes.
If the function is passed a valid PIN string, return true, else return false.
"""

#code 1
import re 

pin=input("Enter your ATM pin : ")

def validate_pin(pi): 
    return bool(re.fullmatch("\d{4}|\d{6}", pi))

#code 2
def ATM_pin(p): 
    return len(p) in (4, 6) and p.isdigit()

#code 3
def validate(pin):
    if len(pin) == 4 or len(pin) == 6: 
        if re.search('[^0-9]', pin) == None : 
            return True

print(validate_pin(pin))

print(ATM_pin("123567"))

print(validate("3453"))

