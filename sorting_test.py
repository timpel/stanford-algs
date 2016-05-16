import mergesort.merge_sort
import quicksort.quicksort
import sys
import time
from random import randint

def multi_size(max_len):

	for n in [2**(n+1) for n in range(max_len)]:
		print 'Array size: %d' % n
		arr = [randint(0, 2**max_len) for n in range(n)]
		
		current_time = time.time()
		quicksort.quicksort.check(mergesort.merge_sort.sort(arr), n+1)
		print 'Merge sort: %f' % (time.time() - current_time)

		current_time = time.time()
		quicksort.quicksort.check(quicksort.quicksort.sort(arr), n+1)
		print 'Quicksort: %f' % (time.time() - current_time)
		print '-----------------'

def fixed_time(sec, length, sort_func, func_name):

	count = 0
	start = time.time()
	end = start + sec

	while time.time() < end:
		arr = [randint(0, length) for n in range(length)]
		sort_func(arr)
		count += 1

	print '%s sort: %d %d-element arrays in %d seconds' % (func_name, count, length, sec)

if __name__ == '__main__':

	if len(sys.argv) > 2:
		fixed_time(int(sys.argv[1]), int(sys.argv[2]), mergesort.merge_sort.sort, 'Merge')
		fixed_time(int(sys.argv[1]), int(sys.argv[2]), quicksort.quicksort.sort, 'Quick')
	else:
		multi_size(int(sys.argv[1]))