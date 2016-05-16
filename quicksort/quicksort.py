from random import randint
import sys

def sort(arr):
	length = len(arr)
	pivot_index = randint(0, length-1)
	pivot = arr[pivot_index]
	swap(arr, 0, pivot_index)

	i = j = 1

	while j < length:
		if arr[j] < pivot:
			swap(arr, j, i)
			i += 1
		j += 1

	swap(arr, 0, i-1)

	first_part = arr[:i-1]
	second_part = arr[i:]

	if i > 2:
		first_part = sort(first_part)

	if length - i > 1:
		second_part = sort(second_part)

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

	unsorted = [randint(0, arr_len) for n in range(arr_len)]
	length = len(unsorted)
	check(sort(unsorted), length)


if __name__ == '__main__':

	try:
		arr_len = int(sys.argv[1])
	except (IndexError, ValueError):
		print 'Format: python quicksort.py <array-length>'

	main(arr_len)
