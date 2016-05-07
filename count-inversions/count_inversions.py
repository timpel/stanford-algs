from random import randint
import sys

def sort_and_count(arr):
	n = len(arr)

	if n == 1:
		return arr

	else:
		first_half = arr[:n/2]
		second_half = arr[n/2:]
		return merge_and_count_split(sort_and_count(first_half), sort_and_count(second_half))


def merge_and_count_split(arr1, arr2):
	i, j = 0, 0
	result = []

	while 1:
		if i == len(arr1):
			result.extend(arr2[j:])
			break
		if j == len(arr2):
			result.extend(arr1[i:])
			break

		if (arr1[i] < arr2[j]):
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1

	return result

def main(arr_len):
	test_arr = [randint(0,arr_len) for n in range(arr_len)]
	return sort_and_count(test_arr)

if __name__ == '__main__':
	try:
		arr_len = int(sys.argv[1])
	except (IndexError, ValueError):
		print 'Format: python merge-sort.py <array-length>'

	print main(arr_len)