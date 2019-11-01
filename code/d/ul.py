import numpy as np
from numpy import dot
from numpy.linalg import norm

# [i] > 0
def v_gi(v):
	return np.where(v.reshape(v.size) > 0.0)[0]

def cos(v1, v2):
	tmp = norm(v1) * norm(v2)
	return dot(v1, v2) / tmp if tmp > 0 else 0
def dis(v1, v2):
	return norm(v1 - v2)


def c_sim(v1, v2):
	return cos(v1, v2)
def u_sim(v1, v2):
	return cos(v1, v2)
def l_sim(v1, v2):
	return 1 / (1 + dis(v1, v2))
def z_sim(v1, v2):
	return 1 / (1 + dis(v1, v2))
