from d.dt import dt
from d.t import t
from mp.g import g
from rw.cw import cw
from rw.cs import cs
from rw.be import be
from d.g.wv import t_cv, t_uv
from d.ul import c_sim, u_sim, l_sim, z_sim

class sr:
	rn = int(30 * 3)

	def __init__(self, p):
		self.p = p
		if self.p.m == "our":
			self.g = g(p)
		elif self.p.m == "cs":
			self.g = cs(p)
		elif self.p.m == "cw":
			self.g = cw(p)
		elif self.p.m == "be":
			self.g = be(p)


	def run(self):
		q = self.g.run()
		r = self.run2(q)

		return q, r

	def run2(self, q):
		t_ = dt.t
		t_ = t(t_.v[t_.c[:, q.c] > 0.0])

		qc = t_cv.v[q.c] # wv
		qu = t_uv.v[q.u] # wv

		if len(t_.v) > self.rn:
			w = {}
			for i, (c2, u2, l, z) in enumerate(zip(t_.c2, t_.u2, t_.l, t_.z)):
				w[i] = c_sim(qc, c2) + \
					   u_sim(qu, u2) + \
					   l_sim(q.l, l) + \
					   z_sim(q.z, z)

			o = sorted(w, key=w.get, reverse=True) # max
			return t(t_.v[o[:self.rn]])
		return t_
