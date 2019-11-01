import numpy as np
from p.p import p
from z1.ul import less_t
np.set_printoptions(precision=3)

ln = 500
eid = [116, 27, 264, 184, 217, 49, 119, 175, 112, 180, 131, 93, 101, 245, 100, 33, 69, 68, 6, 129, 98, 233, 209]
#rate = "0.4"

m_ = "cw"
#m_ = "cs"
#m_ = "be"

s = []
for i in eid:
	#less_t(i, rate)

	p_ = p(i, m_)
	for _ in range(ln):
		p_.run()
	s.append(p_.get_re())
	p_.cl()
	print("{} {}".format(s[-1], p_.eid))

#print(rate)
print(np.array(s).mean(axis=0).tolist())
