import copy
import numpy as np
from d.de import de
from d.g.wv import t_cv, to_wv
from d.t import t
from d.ul import v_gi, c_sim
from mp.g import g

class cs(g):
	sc_low = 0.25

	def __init__(self, p):
		self.p = p
		self.c = {}
		self.ec = to_wv(de.to_t(self.p.e.c[0]), t_cv.v)

	def run(self):
		q = copy.copy(self.p.q_[-1])

		q.c = self.c_lim(self.c_pick())
		q = cs.q_m(q, self.p)

		return q

	def c_pick(self):
		t_ = self.p.t1()
		r = []
		for i, c2 in enumerate(t_.c2):
			sc = c_sim(c2, self.ec)
			if sc >= self.sc_low:
				r.append(i)
		t2_ = t(t_.v[r])

		v = t2_.c_m()
		w = {i: v[i] for i in v_gi(v)}
		o = sorted(w, key=w.get, reverse=True)  # max
		return o

	@staticmethod
	def q_m(q, p):
		t_ = p.t1()
		q.u = np.argmax(t_.u_m())
		q.l = t_.l_m()
		q.z = t_.z_m()
		return q
