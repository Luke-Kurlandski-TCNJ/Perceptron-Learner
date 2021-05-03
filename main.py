"""
Run the perceptron learning tasks and the learning problems.
"""

import random

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
	
	weights = [0,0,0,0]
	data = process_iris_data(path='iris.data')
	task = 4

	random.shuffle(data)
	learning_problems(weights=weights, data=data, task=task)

	random.shuffle(data)
	learning_problems(weights=weights, data=data, task=task)

def task3():
	"""
	Setup learning environment as specified for task 3.
	"""
	import csv 

	data_flower = csv.DictReader(open('iris.csv', 'r'))
	dict_lists = []

	for line in data_flower:
		dict_lists.append(line)

	##task 3, part 1, dataset 1
	t3_1_1 = Perceptron(name = 'Iris-setosa', weights=[1,1,1,1,1])
	t3_1_1.fit(dict_lists, path=f'D3_1_iris_setosa_stats.csv')

	t3_1_2 = Perceptron(name = 'Iris-versicolor',weights=[1,1,1,1,1])
	t3_1_2.fit(dict_lists, path=f'D3_1_iris_versicolor_stats.csv')

	t_3_3 = Perceptron(name = 'Iris-virginica',weights=[1,1,1,1,1])
	t_3_3.fit(dict_lists, path=f'D3_1_iris_virginica_stats.csv')

	##task 3, part 2
	t3_2_1 = Perceptron(name = 'Iris-setosa', weights=[.1,.2,.3,.4,.5])
	t3_2_1.fit(dict_lists, path=f'D3_2_iris_setosa_stats.csv')

	t3_2_2 = Perceptron(name = 'Iris-versicolor',weights=[.1,.2,.3,.4,.5])
	t3_2_2.fit(dict_lists, path=f'D3_2_iris_versicolor_stats.csv')

	t_2_3 = Perceptron(name = 'Iris-virginica',weights=[.1,.2,.3,.4,.5])
	t_2_3.fit(dict_lists, path=f'D3_2_iris_virginica_stats.csv')

	import random
	random_weights = []
	for i in range(5):
    	
		random_weights.append(random.uniform(0.0,1.0))

	t3_3_1 = Perceptron(name = 'Iris-setosa', weights=random_weights)
	t3_3_1.fit(dict_lists,path=f'D3_3_iris_setosa_stats.csv')

	t3_3_2 = Perceptron(name = 'Iris-versicolor',weights=random_weights)
	t3_3_2.fit(dict_lists, path=f'D3_3_iris_versicolor_stats.csv')

	t_3_3 = Perceptron(name = 'Iris-virginica',weights=random_weights)
	t_3_3.fit(dict_lists, path=f'D3_3_iris_virginica_stats.csv')	

	pass 

def task2():
	"""
	Setup learning environment as specified for task 2.
	"""
	import csv 

	data_flower = csv.DictReader(open('iris.csv', 'r'))
	dict_lists = []

	for line in data_flower:
		dict_lists.append(line)

	lp1 = Perceptron(name = 'Iris-setosa')
	lp1.fit(dict_lists, path=f'D2_iris_setosa_stats.csv')

	lp2 = Perceptron(name = 'Iris-versicolor')
	lp2.fit(dict_lists, path=f'D2_iris_versicolor_stats.csv')

	lp3 = Perceptron(name = 'Iris-virginica')
	lp3.fit(dict_lists, path=f'D2_iris_virginica_stats.csv')

	pass


def main():
	"""
	
	""" 
	task2()
	pass

if __name__ == "__main__":
	main()