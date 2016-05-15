import mergesort.merge_sort
import quicksort.quicksort
import sys
import time
from random import randint

def main(max_len):

	for n in [2**(n+1) for n in range(max_len)]:
		print 'Array size: %d' % n
		arr = [randint(0, 2**max_len) for n in range(n)]
		
		current_time = time.time()
		quicksort.quicksort.check(mergesort.merge_sort.sort(arr))
		print 'Merge sort: %f' % (time.time() - current_time)

		current_time = time.time()
		quicksort.quicksort.check(quicksort.quicksort.sort(arr, 0, len(arr)))
		print 'Quicksort: %f' % (time.time() - current_time)
		print '-----------------'

if __name__ == '__main__':

	try:
		max_len = int(sys.argv[1])
	except (IndexError, ValueError):
		print 'Format: python sorting_test.py <log(max input)>'

	main(max_len)