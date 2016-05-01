import time
import sys

def sort(arr, desc):
	l = len(arr)

	# If the array is too large, split it in two and recursively call sort on each half
	# Then merge the arrays once they are sorted
	if l > 2:
		arr1 = arr[:l/2]
		arr2 = arr[l/2:]

		return merge(sort(arr1, desc), sort(arr2, desc), desc)

	# If the array is down to two elements:
	# If the descending flag is false, return a reversed version if the first element is bigger
	# If the descending flag is true, return reversed array if *second* element is bigger
	# Otherwise return the array unchanged
	elif l == 2:
		if (arr[0] > arr[1] and not desc) or (arr[0] < arr[1] and desc):
			return [arr[1], arr[0]]
		else:
			return arr

	# If the array has just one element, return itself
	else:
		return arr

def merge(arr1, arr2, desc):
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

		# Compare values at each pointer
		# Append the lower value (if desc is false) or the higher value (if desc is true) to the merged array
		# Increment the appropriate pointer
		if (arr1[i] < arr2[j] and not desc) or (arr1[i] > arr2[j] and desc):
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1

	return result

def main():
	start_array = [n for n in reversed(range(256000))]

	descending = False

	start_time = time.time()

	# If 'd' or 'D' is specified in command line, switch on the 'sort descending' flag
	if len(sys.argv) > 1 and sys.argv[1] in ['d', 'D']:
		descending = True

	sort(start_array, descending)
	print time.time() - start_time

if __name__ == '__main__':
	main()