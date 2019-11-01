import numpy as np
from mp.mp import mp
from mp.a import a
from z1.ul import less_t
np.set_printoptions(precision=3)

ln = 500
eid = [116, 27, 264, 184, 217, 49, 119, 175, 112, 180, 131, 93, 101, 245, 100, 33, 69, 68, 6, 129, 98, 233, 209]
rate = "0.4"

#a_ = [a.c1, a.c2]
a_ = [a.c1]
aid = []
for _ in range(int(ln/len(a_))):
	aid.extend(a_)

# aid = []
# for _ in range(ln):
# 	aid.append(np.random.choice(a.a[1:], 1)[0])

s = []
for i in eid:
	less_t(i, rate)

	p_ = mp(i)
	for k in aid:
		p_.run(k)
	s.append(np.array(p_.get_re()))
	p_.cl()
	print("{} {}".format(s[-1], p_.eid))

print(rate)
print(np.array(s).mean(axis=0).tolist())
