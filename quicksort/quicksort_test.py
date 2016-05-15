import quicksort
import sys

sys.setrecursionlimit(10000)

for n in [2**n for n in range(15)]:
	quicksort.main(n)