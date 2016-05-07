from random import randint
import sys

def sort_and_count(arr):
	n = len(arr)

	if n == 1:
		return 0

	else:
		first_half = arr[:n/2]
		second_half = arr[n/2:]
		return merge_and_count_split(sort_and_count(first_half), sort_and_count(second_half))


def merge_and_count_split(arr1, arr2):
	return 0

def main(arr_len):
	test_arr = [randint(0,arr_len) for n in range(arr_len)]
	return sort_and_count(test_arr)

if __name__ == '__main__':
	try:
		arr_len = int(sys.argv[1])
	except (IndexError, ValueError):
		print 'Format: python merge-sort.py <array-length>'

	print main(arr_len)