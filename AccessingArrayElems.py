# Accessing array elements

import numpy as np

def test_run():

	a = np.random.rand(5, 4)
	
	print "Array:\n", a

	# Accessing element at position (3, 2)
	element = a[3, 2]

	print element

	# Elements in defined range
	print a[0, 1:3]

	# Top-left corner
	print a[0:2, 0:2]

	# Slicing
	# Note: Slice n:m:t specifies a range that starts at n, and stops before m, in size t
	print a[:, 0:3:2] # will select columns 0, 2 for every row

	# Assigning a value to a particular location
	a[0, 0] = 1
	print "\nModified (replaced one element):\n", a

	# Assigning a single value to an entire row
	a[0,:] = 2
	print "\nModified (replaced a row with a single value):\n", a

	# Assigning a list to a column in an array
	a[:, 3] = [1, 2, 3, 4, 5]
	print "\nModified (replaced a column with a list):\n", a

if __name__ == "__main__":
	test_run()