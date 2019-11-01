import copy
from mp.a import a

class g:

	def __init__(self, p):
		self.p = p
		self.c = {}
		self.u = {}

	def run(self):
		q = copy.copy(self.p.q_[-1])
		o = self.p.a.run()

		if self.p.aid in [a.c1, a.c2]:
			q.c = self.c_lim(o)
		elif self.p.aid in [a.u1, a.u2]:
			q.u = self.u_lim(o)
		elif self.p.aid in [a.l1, a.l2]:
			q.l = o
		elif self.p.aid in [a.z1, a.z2]:
			q.z = o

		return q

	def c_lim(self, o):
		n = 10
		if len(o) > 0:
			for i in o:
				if not i in self.c:
					self.c[i] = 1
					return i
				elif self.c[i] < n:
					self.c[i] += 1
					return i
			#print("c_lim")
			return o[0]
		#print("c no q")
		return 0

	def u_lim(self, o):
		n = 5
		if len(o) > 0:
			for i in o:
				if not i in self.u:
					self.u[i] = 1
					return i
				elif self.u[i] < n:
					self.u[i] += 1
					return i
			#print("u_lim")
			return o[0]
		#print("u no q")
		return 0
