"""
An elementary perceptron as in an artificial nueral network.

Notes
------------------------------------------------------------------------
	What should the default weights of the perceptron be?
"""
import csv 

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

	def __init__(self, name, weights=None):
		"""
		Handle the initialization of the weights for the perceptron.
		"""
		self.targetClass = name
		self.lr = 0.1
		if weights is not None:
			self.weights = weights
		else:
			self.weights = [0,0,0,0,0]

	def fit(self, data, path = None):
		"""
		Learn the data by updating the perceptron's weights.

		Arguments
		----------------------------------------------------------------
			data : list : list of dictionaries containing training instances with the following keys:
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
		epoch = 0
		error = -1
		name = self.targetClass + 'stats.csv'
		if path is None:
			file = open(name, 'w', newline='')
		else:
			file = open(path, 'w', newline='')
		write = csv.writer(file)
		write.writerow(["epoch", "error", "weights"])

		while error != 0 and epoch < 100:
			epoch += 1
			error = 0
			for dict in data:
				target = 1 if (self.targetClass == dict['class']) else -1
				x = [1]
				for key in dict.keys():
					if key != "class":
						x.append(float(dict[key]))
				diff = target - self.output(x)
				if diff != 0:
					error += 1
				for i in range(len(self.weights)):
					delta = self.lr * diff * x[i]
					self.weights[i] = self.weights[i] + delta 
			row = [epoch,error,self.weights]
			write.writerow(row)	
			 

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
		sum = 0
		for i in range(len(self.weights)):
			sum += self.weights[i] * x[i]
		z = 1 if (sum > 0) else -1
		return z

	
	
