from random import randint
import sys
import time

def sort(arr, start, length):

	if length <= 1:
		return arr

	pivot_index = randint(start, length-1)
	pivot = arr[pivot_index]
	swap(arr, start, pivot_index)

	i = j = start + 1

	while j < length:
		if arr[j] < pivot:
			swap(arr, j, i)
			i += 1
		j += 1

	swap(arr, start, i-1)

	first_part = sort(arr[start:i], start, i)
	second_part = sort(arr[i:length], start, length - i - 1)

	return first_part + second_part


def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp

def check(arr):
	print arr
	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]:
			return False
	return True

def main(arr_len):

	unsorted = [randint(0, 100) for n in range(arr_len)]
	start_time = time.time()
	print check(sort(unsorted, 0, len(unsorted)-1))


if __name__ == '__main__':

	try:
		arr_len = int(sys.argv[1])
	except (IndexError, ValueError):
		print 'Format: python quicksort.py <array-length>'

	main(arr_len)
