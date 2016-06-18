# Array attributes

import numpy as np

def test_run():

	a = np.random.random((5,4)) # 5x4 array of random numbers
	print a

	print a.dtype # datatype of values in array a

	print a.shape # shape of array
	print a.shape[0] # number of rows
	print a.shape[1] # number of columns

	print len(a.shape) # dimension of array

	print a.size # number of elements in array

if __name__ == "__main__":
	test_run()