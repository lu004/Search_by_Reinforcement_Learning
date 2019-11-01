import numpy as np
from d.ul import dis
from d.g.wv import t_cv, t_uv, to_wv

class s:

	st = ["d_c", "d_u", "d_l", "d_z",
		  "d2_c", "d2_u", "d2_l", "d2_z",
		  "r", "n"]

	def __init__(self, p):
		self.p = p

	def run(self):  # state

		t_ = self.p.t1()
		t2_ = self.p.t2()
		t_r = self.p.t1_r()
		t2_r = self.p.t2_r()

		o = np.array([
			self.d_c(t_, t2_),
			self.d_u(t_, t2_),
			self.d_l(t_, t2_),
			self.d_z(t_, t2_),

			self.d_c(t_r, t2_r),
			self.d_u(t_r, t2_r),
			self.d_l(t_r, t2_r),
			self.d_z(t_r, t2_r),

			self.r(t_r, t2_r),
			self.n(t_)])

		return o

	def d_c(self, t_, t2_):
		v1 = to_wv(t_.c_m(), t_cv.v)
		v2 = to_wv(t2_.c_m(), t_cv.v)
		return dis(v1, v2)

	def d_u(self, t_, t2_):
		v1 = to_wv(t_.u_m(), t_uv.v)
		v2 = to_wv(t2_.u_m(), t_uv.v)
		return dis(v1, v2)

	def d_l(self, t_, t2_):
		return dis(t_.l_m(), t2_.l_m())

	def d_z(self, t_, t2_):
		return dis(t_.z_m(), t2_.z_m())

	def r(self, t_, t2_):
		return len(t_.v) - len(t2_.v)
	def n(self, t_):
		n1 = sum(np.isin(t_.ti, list(self.p.ti.keys()), invert=True))
		return n1
