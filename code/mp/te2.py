import numpy as np
import os
from d.d import d
from d.dt import dt
from mp.te import te
from z.no_we.m3 import m3, te_sc3

class te2(te):
	sc_low = 0.4

	def te_load(self):
		self.g = d.te_g
		p = os.path.join(m3.dd, "te_{}.npy".format(self.ds))
		if os.path.exists(p):
			self.c = np.load(p)
			print("ld:" + p)
		else:
			m_ = m3()
			self.c, _ = te_sc3(m_, dt.t, self.g)
			np.save(p, self.c)

		self.rnk_t()
		#self.rnk_e()
		print("te:{}".format(len(self.t_r)))