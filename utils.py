"""
Useful functions for data extraction.
"""

import pprint
import csv

def process_iris_data(path='iris.data', verbose=False):
	"""
	Process the iris data from file and return python object.

	Arguments
	--------------------------------------------------------------------
		path : str : location of comma separated iris data
		verbose : bool : if True, prints out the data prior to returning

	Returns
	--------------------------------------------------------------------
		data : [{}] : a list of iris data, each element is an individual
			example implemented as a dictionary with the following keys:
			'sepal_length', 
			'sepal_width', 
			'petal_length', 
			'petal_width', 
			'class'
	"""

	fieldnames = [
		'sepal_length', 
		'sepal_width', 
		'petal_length', 
		'petal_width', 
		'class'
	]

	with open(path, newline='') as csvfile:
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)
		data = list(map(lambda x: dict(x), reader))

	if verbose:
		pprint.pprint(data)

	return data