import numpy as np
def make_transpose(m):
	return np.array(m) \
	.T \
	.tolist()
	
make_transpose([[1,2],[3,4],[5,6],[7,8],[9,10]])