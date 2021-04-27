"""
Learning scheduling algorithms to be used in the perceptron learning.
"""

def exponential_decay(epoch, lr_initital=.01, base=.1, n_steps=20):
	"""
	Exponential learning rate decay.

	Arguments
	--------------------------------------------------------------------
		epoch : int : the current training epoch
		lr_initial : float : the initial learning rate used
		base : float : base for the exponential decay
		n_steps : int : slash learning rate by base times every n_steps

	Returns
	--------------------------------------------------------------------
		float : the adjusted learning rate
	"""

	return lr_initital * base**(epoch / n_steps)