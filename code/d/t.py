import numpy as np
from d.g.tf import tf

class t:
	i = [3, tf.f_n, 274, tf.f_n, 321, 2, 1]  # ccuulz
	#i = [3, tf.f_n, 0, tf.f_n, 0, 2, 1]  # culz

	def __init__(self, v=None):
		self.v = v if (not v is None) and (len(v) > 0) else self.zero()

		self.ti, self.ei, self.rf = self.v[:, 0], self.v[:, 1], self.v[:, 2]
		k = 1
		self.c = self.v[:, sum(self.i[:k]): sum(self.i[:k+1])]
		k = 2
		self.c2 = self.v[:, sum(self.i[:k]): sum(self.i[:k+1])]
		k = 3
		self.u = self.v[:, sum(self.i[:k]): sum(self.i[:k+1])]
		k = 4
		self.u2 = self.v[:, sum(self.i[:k]): sum(self.i[:k+1])]
		k = 5
		self.l = self.v[:, sum(self.i[:k]): sum(self.i[:k+1])]
		k = 6
		self.z = self.v[:, sum(self.i[:k]): sum(self.i[:k+1])]

	def c_(self, c):
		self.c = c
		self.mer()
	def c2_(self, c2):
		self.c2 = c2
		self.mer()
	def u_(self, u):
		self.u = u
		self.mer()
	def u2_(self, u2):
		self.u2 = u2
		self.mer()
	def l_(self, l):
		self.l = l
		self.mer()
	def z_(self, z):
		self.z = z
		self.mer()
	def mer(self):
		self.v = np.c_[self.v[:, :3], self.c, self.c2, self.u, self.u2, self.l, self.z]

	def cnt(self):
		return np.c_[self.c2, self.l, self.z]

	def gt(self, ti):
		return t(self.v[np.isin(self.ti, ti)])
	def ge(self, ei):
		return t(self.v[np.isin(self.ei, ei)])

	def c_m(self):
		return np.mean(self.c, axis=0)
	def u_m(self):
		return np.mean(self.u, axis=0)
	def l_m(self):
		return np.mean(self.l, axis=0)
	def z_m(self):
		return np.mean(self.z, axis=0)

	@staticmethod
	def zero():
		return np.zeros([1, sum(t.i)])
