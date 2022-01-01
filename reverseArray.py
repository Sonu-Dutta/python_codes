# Iterative python program to reverse an array
def rvArray(a, start, end):
	while start < end:
		a[start], a[end] = a[end], a[start]
		start += 1
		end -= 1
arr = [1, 2, 3, 4, 5, 6]
print("Original array is")
print(arr)
rvArray(arr, 0, 5)
print("Reversed array is")
print(arr)