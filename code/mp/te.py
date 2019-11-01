import numpy as np
import os
from d.d import d
from d.dt import dt
from te.m import m, te_sc

class te:
	#top = 8
	sc_low = 0.4
	ds = "test"

	def __init__(self, eid):
		self.eid = eid
		self.te_load()

	def pd(self, t_):
		return t_.gt(self.t_r)

	def te_load(self):
		self.g = d.te_g # test
		p = os.path.join(m.dd, "te_{}.npy".format(self.ds))
		if os.path.exists(p):
			self.c = np.load(p)
			print("ld:" + p)
		else:
			m_ = m()
			self.c, _ = te_sc(m_, dt.t, self.g)
			np.save(p, self.c)

		self.rnk_t()
		#self.rnk_e()
		print("te:{}".format(len(self.t_r)))

	def rnk_t(self):
		self.t_r = []
		e = np.where(self.g.ei == self.eid)[0][0]
		for c_, i in zip(self.c[:, e], dt.t.ti):
			if c_ >= self.sc_low:
				self.t_r.append(i)

	def rnk_e(self):
		self.t_r = []
		for c_, i in zip(self.c, dt.t.ti):
			if self.eid in self.g.ei[np.argsort(c_)[::-1]][:self.top]:
				self.t_r.append(i)
