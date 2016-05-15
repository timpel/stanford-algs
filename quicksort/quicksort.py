from random import randint

def sort(arr, start, length):

	if length <= 1:
		return arr

	pivot = choose_pivot(arr, length)
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


def choose_pivot(arr, length):

	return arr[0]


if __name__ == '__main__':
	
	unsorted = [randint(0, 100) for n in range(100)]
	print sort(unsorted, 0, len(unsorted)-1)
