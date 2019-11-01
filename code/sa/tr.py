import numpy as np
import gc
from mp.a import a
from sa.m import m
from collections import namedtuple
np.set_printoptions(precision=3)
r = namedtuple("r", ["s", "ai", "d", "s2"])

class tr:
	seq_n = m.seq_n
	eps = 0.15
	d_long = 0.8
	r_n = 100

	n = 5
	l_max = 500
	def __init__(self, p):
		self.p = p
		self.m = m()
		self.m2 = m()

	def run(self):
		re = []
		self.r = []
		for _ in range(int(self.r_n)):
			self.a_pick()

		for _ in range(self.n):
			self.p.reset()
			for l in range(self.l_max):
				if l % self.r_n == 0:
					self.tr()
				if l % (self.r_n * 2) == 0:
					self.m2.m = self.m.cp()
				self.a_pick()

			re.append(self.p.get_re())
			#re.append(self.p.d_)
			#print("{}:{}".format(re[-1], self.p.eid))

		#self.m.sv()
		return re


	def tr(self):
		size = len(self.r)
		if size >= 1:
			s_ = []
			g_ = []
			for k in np.random.choice(range(size), int(size), replace=False):
			#for k in range(size):
				r_ = self.r[k]
				s, ai, d, s2 = r_.s, r_.ai, r_.d, r_.s2

				s2 = np.expand_dims([s2], axis=0)
				q_a = self.m.m.predict(s2)[0]
				q_v = self.m2.m.predict(s2)[0]
				q_max = q_v[np.argmax(q_a)]
				td = d + self.d_long * np.array(q_max)

				g = np.zeros(len(a.a))
				g[a.m[ai]] = td

				s_.append(s)
				g_.append(g)

			#print(len(s_))
			self.m.m.fit(np.array(s_), np.array(g_),
						 batch_size=16, epochs=5, verbose=0)

	def a_pick(self):
		s = self.seq()

		q = self.m.m.predict(np.expand_dims(s, axis=0))[0]
		pr = np.ones(len(a.a), dtype=float) * self.eps / len(a.a)
		pr[np.argmax(q)] += (1.0 - self.eps)
		ai = np.random.choice(a.a, p=pr)

		_, ai, d, s2 = self.p.run(ai)
		if len(self.r) == self.r_n: self.r.pop(0)
		self.r.append(r(s, ai, d, s2))

	def seq(self):
		s = np.array(self.p.s_[-self.seq_n:])
		if len(s) < self.seq_n:
			s = np.r_[np.zeros([self.seq_n-len(s), len(self.p.s.st)]), s]
		return s


	def cl(self):
		self.p.cl()
		self.m.cl()
		self.m2.cl()
		gc.collect()
