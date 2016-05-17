import quicksort.quicksort
import random_selection.random_selection
import sys
import time
from random import randint

def main(max_len, check):
	for n in [2**(n+1) for n in range(max_len)]:
		arr = [randint(0, 2**max_len) for n in range(n)]

		median = int(((n+1)+1)/2) - 1

		current_time = time.time()
		result = random_selection.random_selection.select(arr, median)
		end_time = time.time() - current_time

		if check:
			sorted_arr = quicksort.quicksort.sort(arr)

			if sorted_arr[median] == result:
				print "Success! Length: %d -- Time: %f" % (n+1, end_time)

			else:
				print "Failed"

		else:
			print "Length: %d -- Time: %f" % (n+1, end_time)

	return

if __name__ == '__main__':
		arr_len = int(sys.argv[1])

		if len(sys.argv) > 2:
			main(arr_len, True)
		else:
			main(arr_len, False)