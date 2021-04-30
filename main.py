"""
Run the perceptron learning tasks and the learning problems.
"""

from perceptron import Perceptron
from utils import process_iris_data

def learning_problems(weights, data, task):
	"""
	Acomplish the three learning tasks as outlined in Task 2.

	Tasks
	--------------------------------------------------------------------
		LP 1: iris setosa (+1) versus not iris setosa (-1)
		LP 2: iris versicolor (+1) versus not iris versicolor (-1)
		LP 3: iris virginica (+1) versus not iris virginica (-1)
	
	Arguments
	--------------------------------------------------------------------
		weights : [] : list of weights to use for learning problems
		data : [{}] : a list of iris data, each element is an individual
			example implemented as a dictionary with the following keys:
			'sepal_length', 
			'sepal_width', 
			'petal_length', 
			'petal_width', 
			'class'
		task : int : the task number that this function fulfils

	Notes
	--------------------------------------------------------------------
		Will produce three csv files containing the stats for this task.
	"""

	p = Perceptron(name='iris_setosa', weights=weights)
	p.fit(data=data, path=f'D{task}_iris_setosa_stats.csv')

	p = Perceptron(name='iris_versicolor', weights=weights)
	p.fit(data=data, path=f'D{task}_iris_versicolor_stats.csv')

	p = Perceptron(name='iris_virginica', weights=weights)
	p.fit(data=data, path=f'D{task}_iris_virginica_stats.csv')

def task4():
	"""
	Setup learning environment as specified for task 4.
	"""
	
	pass

def task3():
	"""
	Setup learning environment as specified for task 3.
	"""
	
	pass

def task2():
	"""
	Setup learning environment as specified for task 2.
	"""
	
	pass

def main():
	"""
	
	"""

	pass

if __name__ == "__main__":
	main()