def sort(arr, length):
	
	if length == 1:
		return

	pivot = choose_pivot(arr, length)

	return (arr, length, pivot)


def choose_pivot(arr, length):

	return arr[0]


if __name__ == '__main__':
	
	unsorted = list(reversed(range(1000)))
	initial_len = len(unsorted)
	
	print sort(unsorted, initial_len)