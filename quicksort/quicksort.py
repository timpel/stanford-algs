from random import randint
import sys
import time

def sort(arr, start, length):
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

	if i > 2:
		first_part = sort(arr[start:i-1], start, i-1)
	else:
		first_part = arr[start:i-1]

	if length - i > 1:
		second_part = sort(arr[i:length], start, length - i)
	else:
		second_part = arr[i:length]

	return first_part + [arr[i-1]] + second_part


def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp

def check(arr, length):

	if length != len(arr):
		print 'Array size changed!'
		return False

	for i in range(length-1):
		if arr[i] > arr[i+1]:
			print 'Sort Failed!'
			return False
	return True

def main(arr_len):

	unsorted = [randint(0, 100) for n in range(arr_len)]
	start_time = time.time()
	length = len(unsorted)
	check(sort(unsorted, 0, length), length)


if __name__ == '__main__':

	try:
		arr_len = int(sys.argv[1])
	except (IndexError, ValueError):
		print 'Format: python quicksort.py <array-length>'

	main(arr_len)
