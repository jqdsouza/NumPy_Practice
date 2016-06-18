# Accessing elements

import numpy as np

def test_run():

	a = np.random.rand(5)

	# accessing using list of indices
	indices = np.array([1, 1, 2, 3])

	print a[indices]

	b = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
	print b

	# calculating mean
	mean = b.mean()
	print mean

	# masking
	print b[b<mean]

	# can swap vales less than mean with mean value!
	b[b<mean] = mean
	print b


if __name__ == "__main__":
	test_run()