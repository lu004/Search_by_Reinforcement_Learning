import copy
import os
import numpy as np
from d.t import t
from d.dt import dt
from d.g.wv import e_cv, to_wv
from d.ul import v_gi, c_sim
from mp.g import g
from rw.cs import cs
from rw.be_.m import m

class be(g):
	sc_low = 0.15
	ds = "test"

	def __init__(self, p):
		self.p = p
		self.c = {}
		self.ec = self.p.e.c2[0]

		self.be_load()
		self.m = m()

	def run(self):
		q = copy.copy(self.p.q_[-1])

		q.c = self.c_lim(self.c_pick())
		q = cs.q_m(q, self.p)

		return q

	def c_pick(self):
		t_ = self.p.t1()
		r = []
		e_ = self.pd(t_)
		for i, ec in enumerate(e_):
			sc = c_sim(ec, self.ec)
			if sc >= self.sc_low:
				r.append(i)
		t2_ = t(t_.v[r])

		v = t2_.c_m()
		w = {i: v[i] for i in v_gi(v)}
		o = sorted(w, key=w.get, reverse=True)  # max
		return o

	def pd(self, t_):
		r = []
		for i, c in zip(t_.ti, t_.c):
			if i in self.be:
				r.append(self.be[i])
			else:
				r.append(to_wv(self.m.pd(c), e_cv.v))
		return r

	def be_load(self):
		p = os.path.join(m.dd, "be_{}.npy".format(self.ds))
		if os.path.exists(p):
			e_ = np.load(p)
			print("ld:" + p)
		else:
			m_ = m()
			e_ = np.array([to_wv(m_.pd(i), e_cv.v) for i in dt.t.c])
			np.save(p, e_)

		self.be = {}
		for i, v in zip(dt.t.ti, e_):
			self.be[i] = v

	def cl(self):
		self.m.cl()
