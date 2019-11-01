import numpy as np
from mp.mp import mp
from sa.tr import tr
from sa.m import m
from z1.ul import less_t
np.set_printoptions(precision=3)

eid = [116, 27, 264, 184, 217, 49, 119, 175, 112, 180, 131, 93, 101, 245, 100, 33, 69, 68, 6, 129, 98, 233, 209]
rate = "0.6"
s = []
for i in eid:
	less_t(i, rate)
	m.seq_n = 1

	tr_ = tr(mp(i))
	s_ = tr_.run()
	s.append(s_[np.argmax(np.array(s_)[:, 0])])
	tr_.cl()
	print("{} {}".format(s[-1], i))

print(rate)
print(np.array(s).mean(axis=0).tolist())
