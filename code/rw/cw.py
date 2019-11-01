import copy
import numpy as np
from d.dt import dt
from d.ul import v_gi
from d.g.tf import tf
from mp.g import g
from rw.cs import cs

class cw(g):
	d_f = dt.t.c_m()
	w1, w2, w3 = 1.0, 1.0, 1.0

	def __init__(self, p):
		self.p = p
		self.c = {}
		self.c_f = np.zeros(tf.f_n)

	def run(self):
		q = copy.copy(self.p.q_[-1])

		q.c = self.c_lim(self.c_pick())
		q = cs.q_m(q, self.p)

		self.c_f[q.c] += 1 # cnt
		return q

	def c_pick(self):
		v = self.p.t1().c_m()
		f = 1/(self.c_f+1)

		s = self.w1 * v/sum(v) + \
			self.w2 * self.d_f/sum(self.d_f) + \
			self.w3 * f/sum(f)

		w = {i: s[i] for i in v_gi(v)}
		o = sorted(w, key=w.get, reverse=True)  # max
		return o
