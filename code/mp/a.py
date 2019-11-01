import numpy as np
from d.ul import v_gi, l_sim, z_sim

class a:

	c1 = "c_1" # 2 explore
	c2 = "c_2"
	u1 = "u_1"
	u2 = "u_2"
	l1 = "l_1"
	l2 = "l_2"
	z1 = "z_1"
	z2 = "z_2"

	a = [c1, c2, u1, u2, l1, l2, z1, z2]
	m = {v: i for i, v in enumerate(a)}

	def __init__(self, p):
		self.p = p

	def run(self): # type, q, w
		if self.p.aid == a.c1:
			return self.c_1()
		elif self.p.aid == a.c2:
			return self.c_2()
		elif self.p.aid == a.u1:
			return self.u_1()
		elif self.p.aid == a.u2:
			return self.u_2()
		elif self.p.aid == a.l1:
			return self.l_1()
		elif self.p.aid == a.l2:
			return self.l_2()
		elif self.p.aid == a.z1:
			return self.z_1()
		elif self.p.aid == a.z2:
			return self.z_2()

	def c_1(self):
		v = self.p.t1().c_m()
		v2 = self.p.t1_r().c_m()
		#v2 = v2 * 0
		s = v * (v2 + 0.1)
		w = {i: s[i] for i in v_gi(v)}
		o = sorted(w, key=w.get, reverse=True)  # max
		return o
	def c_2(self):
		v = self.p.t1().c_m()
		v2 = self.p.t1_r().c_m()
		#v2 = v2 * 0
		s = (1/(v+0.1)) * (v2 + 0.1)
		w = {i: s[i] for i in v_gi(v)}
		o = sorted(w, key=w.get, reverse=True)
		return o

	def u_1(self):
		v = self.p.t1().u_m()
		v2 = self.p.t1_r().u_m()
		s = v * (v2 + 0.1)
		w = {i: s[i]+1 for i in v_gi(v)}
		o = sorted(w, key=w.get, reverse=True)
		return o
	def u_2(self):
		v = self.p.t1().u_m()
		v2 = self.p.t1_r().u_m()
		s = (1/(v+0.1)) * (v2 + 0.1)
		w = {i: s[i]+1 for i in v_gi(v)}
		o = sorted(w, key=w.get, reverse=True)
		return o

	def l_1(self):
		l = self.p.t1().l
		m = np.mean(l, axis=0)
		# l2 = self.p.t1_r().l
		# if len(l2) >= 2:
		# 	m = (m+np.mean(l2, axis=0))/2
		w = {i: l_sim(l[i], m) for i in range(len(l))}
		o = sorted(w, key=w.get, reverse=True)
		return l[np.random.choice(o[:3], 1)[0]]
	def l_2(self):
		l = self.p.t1().l
		m = np.mean(l, axis=0)
		# l2 = self.p.t1_r().l
		# if len(l2) >= 2:
		# 	m = (m+np.mean(l2, axis=0))/2
		w = {i: l_sim(l[i], m) for i in range(len(l))}
		o = sorted(w, key=w.get, reverse=False)
		return l[np.random.choice(o[:3], 1)[0]]

	def z_1(self):
		z = self.p.t1().z
		m = np.mean(z)
		# z2 = self.p.t1_r().z
		# if len(z2) >= 2:
		# 	m = (m+z2.mean())/2
		w = {i: z_sim(z[i], m) for i in range(len(z))}
		o = sorted(w, key=w.get, reverse=True)
		return z[np.random.choice(o[:3], 1)[0]]
	def z_2(self):
		z = self.p.t1().z
		m = np.mean(z)
		# z2 = self.p.t1_r().z
		# if len(z2) >= 2:
		# 	m = (m+z2.mean())/2
		w = {i: z_sim(z[i], m) for i in range(len(z))}
		o = sorted(w, key=w.get, reverse=False)
		return z[np.random.choice(o[:3], 1)[0]]
