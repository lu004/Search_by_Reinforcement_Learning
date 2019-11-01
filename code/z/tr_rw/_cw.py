import numpy as np
from p.p import p
from rw.cw import cw

ln = 500
eid = [253, 111, 295]
m = "cw"

r2 = {}
for w1 in np.arange(0.1, 1, 0.2):
	for w2 in np.arange(0.1, 1, 0.2):
		for w3 in np.arange(0.1, 1, 0.2):
			cw.w1, cw.w2, cw.w3 = w1, w2, w3

			r = []
			for i in eid:
				p_ = p(i, m)
				for _ in range(ln):
					p_.run()
				r.append(p_.get_re())
				p_.cl()

			r2[(w1, w2, w3)] = np.array(r).mean(axis=0)[0]
			print(r2[(w1, w2, w3)])

print(r2)
