# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([7, 0, 1, 2, 0, 1, 3]) # returns [7, 1, 2, 1, 3, 0, 0]


#  method 1
def move_zero_to_end(num_list):

    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return(x)
print(move_zero_to_end([0,21,0,13,24,46,37,10]))
print(move_zero_to_end([10,0,51,42,0,74,17]))

# method 2

def ZerosToEnd(arr, n):
	count = 0 
	for i in range(n):
		if arr[i] != 0:
			arr[count] = arr[i]
			count+=1
	while count < n:
		arr[count] = 0
		count += 1
		
arr = [14, 21, 42, 0, 0, 73, 0, 46, 0, 89]
n = len(arr)
ZerosToEnd(arr, n)
print("Array after pushing all zeros to end :")
print(arr)


