import os
import json
import numpy as np
from d.g.tf import tf
from d.e import e
from d.ul import v_gi
from d.dt import dd, dt

def e2t_(c):
	m = {}
	for i, w in c.items():
		for i2, w2 in dt.c.items():
			if w == w2:
				m[int(i)] = int(i2)
				break
	return m

class de:
	raw = json.load(open(os.path.join(dd, "e_raw.json")))
	e = e(np.load(os.path.join(dd, "e2.npy")))
	c = json.load(open(os.path.join(dd, "e_c.json")))
	e2t = e2t_(c)

	@staticmethod
	def sh_c(i):
		return [w for i_, w in de.c.items() if int(i_) in i]
	@staticmethod
	def to_t(v):
		r = np.zeros(tf.f_n)
		for i in v_gi(v):
			if i in de.e2t:
				r[de.e2t[i]] = v[i]
		return r
