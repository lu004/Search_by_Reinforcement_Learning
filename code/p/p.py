import numpy as np
from d.dt import dt
from d.de import de
from d.t import t
from p._q import q
from p._sr import sr
from d.g.wv import t_cv, to_wv
np.set_printoptions(precision=3)

class p:

	def __init__(self, eid, m):
		self.m = m
		self.eid = eid
		self.e = de.e.ge(eid)
		self.t = dt.t.ge(eid)
		self.reset()

	def reset(self):
		self.init()

	def init(self):
		self.sr = sr(self)
		self.q_ = [q(c=0, u=0, l=[0.0, 0.0], z=[0.0])]

		t_ = t() # e
		ec = de.to_t(self.e.c[0])
		t_.c_(np.array([ec]))
		t_.c2_(np.array([to_wv(ec, t_cv.v)]))
		self.t_ =[t_]

		self.d = {}
		self.d_ = [0.0]
		self.l = 0

	def run(self):
		self.l += 1 # l=1 start
		q_, t_ = self.sr.run()
		self.upd(q_, t_)


	def upd(self, q_, t_):
		self.q_.append(q_)
		self.t_.append(t_)

		# d
		c = len(self.d)
		for i in self.t1().ge(self.eid).ti:
			self.d[i] = 1
		self.d_.append((len(self.d) - c)/len(self.t.v))


	def t1(self):
		return self.t_[-1]

	def t2(self):
		t_ = self.t_[-2] if len(self.t_) >= 2 else self.t_[-1]
		return t_


	def get_re(self):
		t_ = self.t.gt(list(self.d))
		r = len(t_.v) / len(self.t.v)
		r_i = sum(t_.rf == 2) / len(self.t.v)
		r_e = sum(t_.rf == 1) / len(self.t.v)

		return np.array([r, r_i, r_e])

	def cl(self):
		self.q_.clear()
		self.t_.clear()
		#self.sr.g.cl()

	# def show(self):
	# 	#if self.d_[self.l] > 0.0:
	# 		print("\n{}".format(self.l))
	# 		print("e:{:.0f}".format(self.eid))
	# 		self.q_[self.l].show()
	# 		print("t:{}".format(len(self.t_[self.l].v)))
	# 		print("d_:" + "{:.3f}".format(sum(self.d_)))

