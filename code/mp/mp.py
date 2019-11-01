import numpy as np
from d.dt import dt
from d.de import de
from mp.a import a
from mp.s import s
from mp.te import te
#from mp.te2 import te2
from p.p import p
np.set_printoptions(precision=3)

class mp(p):

	def __init__(self, eid):
		self.m = "our"
		self.eid = eid
		self.e = de.e.ge(eid)
		self.t = dt.t.ge(eid)

		self.te = te(eid)
		self.reset()

	def reset(self):
		self.init()

		self.dr = {}
		self.dr_ = [0.0]
		self.ti = {}

		self.a = a(self)
		self.a_ = [None]
		self.s = s(self)
		self.s_ = [np.zeros(len(s.st)), self.s.run()] # l=1

	def run(self, aid):
		self.l += 1 # l=1 start
		self.aid = aid
		q_, t_ = self.sr.run()
		self.upd(q_, t_)

		#d = self.d_[-1] * len(self.t.v)
		d = self.dr_[-1] # test

		return self.s_[self.l], self.aid, d, self.s_[self.l+1]


	def upd(self, q_, t_):
		self.a_.append(self.aid)
		self.q_.append(q_)
		self.t_.append(t_)
		self.s_.append(self.s.run()) # s next

		# d
		c = len(self.d)
		for i in self.t1().ge(self.eid).ti:
			self.d[i] = 1
		self.d_.append((len(self.d) - c)/len(self.t.v))
		# dr
		c = len(self.dr)
		for i in self.t1_r().ti:
			self.dr[i] = 1
		self.dr_.append(len(self.dr) - c)
		# ti
		for i in self.t1().ti:
			self.ti[i] = 1

	def t1_r(self):
		#return self.t_[-1].ge(self.eid)
		return self.te.pd(self.t_[-1]) # test

	def t2_r(self):
		t_ = self.t_[-2] if len(self.t_) >= 2 else self.t_[-1]
		#return t_.ge(self.eid)
		return self.te.pd(t_) # test

	def cl(self):
		self.q_.clear()
		self.t_.clear()
		self.s_.clear()

	# def show(self):
	# 	#if self.d_[self.l] > 0.0:
	# 		print("\n{}".format(self.l))
	# 		print("e:{:.0f}".format(self.eid))
	# 		print("a:{}".format(self.a_[self.l]))
	# 		self.q_[self.l].show()
	# 		print("t:{}".format(len(self.t_[self.l].v)))
	# 		print("d_:" + "{:.3f}".format(sum(self.d_)))