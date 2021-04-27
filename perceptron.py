"""
An elementary perceptron as in an artificial nueral network.

Notes
------------------------------------------------------------------------
	What should the default weights of the perceptron be?
"""

class Perceptron:
	"""
	An elementary perceptron as in an artificial nueral network.

	Parameters
	--------------------------------------------------------------------
		weights : [] : list of weights for this perceptron; if None,
			uses default weights

	Attributes
	--------------------------------------------------------------------
		weights : [] : list of weights for this perceptron

	Notes
	--------------------------------------------------------------------
	"""

	def __init__(self, weights=None):
		"""
		Handle the initialization of the weights for the perceptron.
		"""

		pass

	def fit(self, data, path):
		"""
		Learn the data by updating the perceptron's weights.

		Arguments
		----------------------------------------------------------------
			data : {} : a dictionary of iris data with following keys:
				'sepal_length', 
				'sepal_width', 
				'petal_length', 
				'petal_width', 
				'class'
			path : str : location to record training data

		Notes
		----------------------------------------------------------------
			Should output a csv file with column headers for the epoch,
				number of errors, etc. as described in requirements
		"""

		pass

	def output(self, x):
		"""
		Output apply sgn step function to weighted sum of feature vec.

		Arguments
		----------------------------------------------------------------
			x : [] : vector of numeric inputs with x_0 = 1

		Returns
		----------------------------------------------------------------
			z : int : sgn(<x, self.weights>), i.e., +1 or -1
		"""

		pass

		