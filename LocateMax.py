# Locate maximum value

import numpy as np

def get_max_index(a):

	#Return the index of the maxmimum value in given 1D array
	return a.argmax()

def test_run():

	a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32) # 32-bit integer array

	print "Array:", a

	#Find the maxmimum and its index in array
	print "Maxmimum value:", a.max()

	print "Index of max.:", get_max_index(a)

if __name__ == "__main__":
	test_run()