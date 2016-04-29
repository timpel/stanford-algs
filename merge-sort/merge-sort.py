from random import randint

def sort(arr):
	l = len(arr)

	# If the array is too large, split it in two and recursively call sort on each half
	# Then merge the arrays once they are sorted
	if l > 2:
		arr1 = arr[:l/2]
		arr2 = arr[l/2:]

		return merge(sort(arr1), sort(arr2))

	# If the array has two elements, return a reversed version if the first element is bigger
	# Otherwise return the array unchanged
	elif l == 2:
		if arr[0] > arr[1]:
			return [arr[1], arr[0]]
		else:
			return arr

	else:
		return arr

def merge(arr1, arr2):
	# Set array traversal pointers to 0
	i, j = 0, 0
	len_1, len_2 = len(arr1), len(arr2)
	result = []

	while 1:
		# If the end of one array is reached, complete the merged array with the rest of the other array
		if i == len_1:
			result.extend(arr2[j:])
			break
		if j == len_2:
			result.extend(arr1[i:])
			break

		# Compare values at each pointer, append the lower value to the merged array and increment the appropriate pointer
		if arr1[i] < arr2[j]:
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1

	return result

def main():
	random_array = [randint(-100, 100) for n in range(100)]
	print random_array
	print sort(random_array)

if __name__ == '__main__':
	main()