"""
Run the perceptron learning tasks and the learning problems.
"""

import random

from perceptron import Perceptron
from plotting import errors_vs_epochs
from utils import process_iris_data

def learning_problems(weights, data, task, stopping_windows=4):
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
		stopping_windows : int : if the mean number of errors from
			the previous stopping_windows epochs is less or equal
			to the mean number of errors from the current 
			stopping_windows epochs, than learning stops

	Notes
	--------------------------------------------------------------------
		Will produce three csv files containing the stats for this task.
	"""

	p = Perceptron(name='Iris-setosa', weights=weights)
	p.fit(data=data, path=f'D{task}_iris_setosa_stats.csv', 
		stopping_windows=stopping_windows)

	p = Perceptron(name='Iris-versicolor', weights=weights)
	p.fit(data=data, path=f'D{task}_iris_versicolor_stats.csv', 
		stopping_windows=stopping_windows)

	p = Perceptron(name='Iris-virginica', weights=weights)
	p.fit(data=data, path=f'D{task}_iris_virginica_stats.csv', 
		stopping_windows=stopping_windows)

	try:
		errors_vs_epochs(
			in1=f'D{task}_iris_setosa_stats.csv', 
			in2=f'D{task}_iris_versicolor_stats.csv', 
			in3=f'D{task}_iris_virginica_stats.csv', 
			output_path=f'D{task}.png'
		)
	except ModuleNotFoundError:
		print("Warning: not making plots")
	except Exception:
		print("An error occurred making plots")

def task4():
	"""
	Setup learning environment as specified for task 4.

	Notes
	--------------------------------------------------------------------
		Training occurs at a slower rate. We find a larger number of
			stopping windows is more effective for this context.
	"""
	
	weights = [0,0,0,0,0]
	data = process_iris_data(path='iris.data')

	random.shuffle(data)
	learning_problems(weights=weights, data=data, task=4.1, 
		stopping_windows=16)

	random.shuffle(data)
	learning_problems(weights=weights, data=data, task=4.2, 
		stopping_windows=16)

def task3():
	"""
	Setup learning environment as specified for task 3.
	"""

	data = process_iris_data(path='iris.data')

	weights = [1,1,1,1,1]
	learning_problems(weights=weights, data=data, task=3.1)

	weights = [.1,.2,.3,.4,.5]
	learning_problems(weights=weights, data=data, task=3.2)

	weights = [random.random() for i in range(5)]
	learning_problems(weights=weights, data=data, task=3.3)

def task2():
	"""
	Setup learning environment as specified for task 2.
	"""
	
	weights = [0,0,0,0,0]
	data = process_iris_data(path='iris.data')

	learning_problems(weights=weights, data=data, task=2)


def main():
	"""
	Perform the tasks.
	""" 
	
	task2()
	task3()
	task4()

if __name__ == "__main__":
	main()
