import numpy as np
import os
from d.ul import v_gi
from d.dt import dd

class t_cv:
	v = np.load(os.path.join(dd, "t_cv.npy"))

class t_uv:
	v = np.load(os.path.join(dd, "t_uv.npy"))

class e_cv:
	v = np.load(os.path.join(dd, "e_cv.npy"))


def to_wv_all(v, wv):
	r = []
	for v_ in v:
		r.append(to_wv(v_, wv))
	return np.array(r)

def to_wv(v, wv):
	v2 = np.zeros(wv.shape[1])
	s = sum(v)
	for i in v_gi(v):
		v2 += (v[i] * wv[i])
	if s > 0.0:
		v2 = v2 / s
	return v2

def gen_co(v, w):
	m = np.zeros([len(w), len(w)])
	for v_ in v:
		i = v_gi(v_)
		for k1 in range(len(i)):
			for k2 in range(k1 + 1, len(i)):
				m[i[k1], i[k2]] += 1
				m[i[k2], i[k1]] += 1
	return m
