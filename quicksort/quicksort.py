def sort(arr, length):
	if length == 1:
		return
	return (arr, length)

if __name__ == '__main__':
	unsorted = list(reversed(range(1000)))
	initial_len = len(unsorted)
	print sort(unsorted, initial_len)