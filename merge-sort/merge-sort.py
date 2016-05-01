import time
import sys

def sort(arr):
	l = len(arr)

	# If the array is too large, split it in two and recursively call sort on each half
	# Then merge the arrays once they are sorted
	if l > 2:
		arr1 = arr[:l/2]
		arr2 = arr[l/2:]

		return merge(sort(arr1), sort(arr2))

	# If the array is down to two elements:
	# Return a reversed version if the first element is bigger
	# Otherwise return the array unchanged
	elif l == 2:
		if (arr[0] > arr[1]):
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
		# If the end of one array is reached, append the rest of the other array
		if i == len_1:
			result.extend(arr2[j:])
			break
		if j == len_2:
			result.extend(arr1[i:])
			break

		# Compare values at each pointer
		# Append the lower value to the merged array
		if (arr1[i] < arr2[j]):
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1

	return result

def main(arr_len, desc):
	start_array = [n for n in reversed(range(arr_len))]

	start_time = time.time()

	# If descending sort is specified, reverse result
	if desc:
		sorted_array = list(reversed(sort(start_array)))

	else:
		sorted_array = sort(start_array)

	print time.time() - start_time

if __name__ == '__main__':
	try:
		arr_len = int(sys.argv[1])
	except (IndexError, ValueError):
		print 'Format: python merge-sort.py <array-length> [d]'

	desc = len(sys.argv) > 2 and sys.argv[2] in ['d', 'D']

	main(arr_len, desc)
