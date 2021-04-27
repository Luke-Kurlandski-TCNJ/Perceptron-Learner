"""
Create the required plots.

To use
------------------------------------------------------------------------
	> python3 plotting.py sample_output.csv sample_plot.png

	or within another python file

	from plotting import errors_vs_epochs
	errors_vs_epochs('sample_output.csv', 'sample_plot.png')

Notes
------------------------------------------------------------------------
	Requires third party library pandas be installed.
"""

import sys

import pandas as pd

def errors_vs_epochs(input_path, output_path):
	"""
	Plot the number of training errors vs the number of epochs.

	Arguments
	--------------------------------------------------------------------
		input_path : str : data collected from perceptron stored in a 
			.csv file with columns: ['epoch','errors', 'weights']
		output_path : str : .png image file to save the plot to
	"""

	df = pd.read_csv(input_path, usecols=['epoch','errors'])
	ax = df.plot.line(x='epoch', y='errors')
	ax.set_xlabel("epoch")
	ax.set_ylabel("# errors")
	ax.figure.savefig('sample_plot.png')

def main():
	if len(sys.argv) < 3:
		print("Read plotting.py, specify input and output.")
	input_path = sys.argv[1]
	output_path = sys.argv[2]
	errors_vs_epochs(input_path, output_path)

if __name__ == "__main__":
	main()