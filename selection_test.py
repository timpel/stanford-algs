import quicksort.quicksort
import random_selection.random_selection
import sys
import time
from random import randint

def main(max_len, check):
	for n in [2**(n+1) for n in range(max_len)]:
		arr = [randint(0, 2**max_len) for n in range(n)]

		median = int((len(arr)+1)/2) - 1

		current_time = time.time()
		result = random_selection.random_selection.select(arr, median)
		end_time = time.time() - current_time

		sorted_arr = quicksort.quicksort.sort(arr)

		if sorted_arr[median] == result:
			print "Success! In %f" % end_time

		else:
			print "Failed"

	return

if __name__ == '__main__':
		arr_len = int(sys.argv[1])
		main(arr_len)