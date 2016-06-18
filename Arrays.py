# Creating NumPy arrays

import numpy as np

def test_run():
	# List to 1D array
	print np.array([2, 3, 4])

	# List of tuples to 2D array
	print np.array([(2, 3, 4), (5, 6, 7)])

	# Empty array
	print np.empty(5)
	print np.empty((5,4))

	# Array of 1s
	print np.ones((5,4))

	# Array of 0s
	print np.zeros((3,3))

	# Specifiying the datatype
	print np.ones((5,4), dtype=np.int_)

if __name__ == "__main__":
	test_run()