import numpy as np
from d.g.tf import tf

class e:
	i = [1, tf.f_n, 204] # cc
	#i = [1, tf.f_n, 0]

	def __init__(self, v=None):
		self.v = v if (not v is None) and (len(v) > 0) else self.zero()

		self.ei = self.v[:, 0]
		self.c = self.v[:, self.i[0]: sum(self.i[:2])]
		self.c2 = self.v[:, sum(self.i[:2]):]

	def c_(self, c):
		self.c = c
		self.mer()
	def c2_(self, c2):
		self.c2 = c2
		self.mer()
	def mer(self):
		self.v = np.c_[self.ei, self.c, self.c2]

	def ge(self, ei):
		return e(self.v[np.isin(self.ei, ei)])

	@staticmethod
	def zero():
		return np.zeros([1, sum(e.i)])