"""
Create the required plots.

To use
------------------------------------------------------------------------

	via the command line:

	> python3 plotting.py in1.csv in2.csv in3.csv output_path.png

	where

		in_1 : str : .csv file for learning problem 1: iris setosa
		in_2 : str : .csv file for learning problem 2: iris versicolor
		in_3 : str : .csv file for learning problem 3: iris virginica
		output_path : str : .png image file to save the plot to

	or via python code:

	from plotting import errors_vs_epochs
	errors_vs_epochs('in1.csv', 'in2.csv', 'in3.csv', 'output_path.png')

Notes
------------------------------------------------------------------------
	Requires third party library pandas be installed.
"""

import sys

try:
	import pandas as pd
except ModuleNotFoundError:
	print("Warning: 'pandas' library not installed for plotting.py")

def errors_vs_epochs(in1, in2, in3, output_path):
	"""
	Plot the number of training errors vs the number of epochs.

	Arguments
	--------------------------------------------------------------------
		in_1 : str : .csv file for learning problem 1: iris setosa
		in_2 : str : .csv file for learning problem 2: iris versicolor
		in_3 : str : .csv file for learning problem 3: iris virginica
		output_path : str : .png image file to save the plot to

	Notes
	--------------------------------------------------------------------
		The csv files should have columns: 'epoch','errors','weights'
	"""

	df1 = pd.read_csv(in1, usecols=['epoch','errors'])
	df2 = pd.read_csv(in2, usecols=['epoch','errors'])
	df3 = pd.read_csv(in3, usecols=['epoch','errors'])

	df1 = df1.rename(columns={"errors": "errors LP 1: iris setosa"})
	df2 = df2.rename(columns={"errors": "errors LP 2: iris versicolor"})
	df3 = df3.rename(columns={"errors": "errors LP 3: iris virginica"})

	df = pd.merge(pd.merge(df1, df2, on='epoch'), df3, on='epoch')

	ax = df.plot.line(x='epoch', y=['errors LP 1: iris setos', 
		'errors LP 2: iris versicolor','errors LP 3: iris virginica'])
	ax.set_xlabel("epoch")
	ax.set_ylabel("# errors")
	ax.figure.savefig(output_path)

def main():
	if len(sys.argv) < 4:
		print("Read plotting.py, specify input and output paths.")

	in1 = sys.argv[1]
	in2 = sys.argv[2]
	in3 = sys.argv[3]
	output_path = sys.argv[4]

	errors_vs_epochs(in1, in2, in3, output_path)

if __name__ == "__main__":
	main()