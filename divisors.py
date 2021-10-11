"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest.
 If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:
divisors(12); #should return [2,3,4,6] divisors(25); #should return [5] """

#code 1
def divisors1(num): 
    l = [a for a in range(2,num) if num%a == 0] 
    if len(l) == 0: 
        return str(num) + " is prime" 
    return l


#code 2

def divisors(integer): 
    a = [] 
    for i in range(2, integer): 
        if integer % i == 0: 
            a.append(i) 
    return a if a else str(integer) + " is prime"



print(divisors(100))