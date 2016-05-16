from random import randint
import sys


def select(arr, order):
	length = len(arr)
	
	if length == 1:
		return arr[0]

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

	pivot_index = i - 1

	if pivot_index == order:
		return pivot

	if pivot_index > order:
		return select(arr[:pivot_index], order)

	if pivot_index < order:
		return select(arr[pivot_index+1:], order - pivot_index -1)


def swap(arr, x, y):

	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp


def main(arr_len, order):

	unsorted = [randint(0, arr_len*10) for n in range(arr_len)]
	length = len(unsorted)
	print (unsorted, select(unsorted, order))


if __name__ == '__main__':

	try:
		arr_len = int(sys.argv[1])
		order_stat = int(sys.argv[2]) - 1
	except (IndexError, ValueError):
		print 'Format: python quicksort.py <array-length> <order-stat>'

	main(arr_len, order_stat)