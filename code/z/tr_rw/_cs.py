import numpy as np
from p.p import p
from rw.cs import cs

ln = 500
eid = [253, 111, 295, 301, 275, 45, 123, 255, 36, 128]
m = "cs"

r2 = {}
for sc in np.arange(0.05, 1.0, 0.05):
	cs.sc_low = sc

	r = []
	for i in eid:
		p_ = p(i, m)
		for _ in range(ln):
			p_.run()
		r.append(p_.get_re())
		p_.cl()
		#print("{} {}".format(r[-1], p_.eid))

	r2[sc] = np.array(r).mean(axis=0)[0]
	print(r2[sc])

print(r2)
