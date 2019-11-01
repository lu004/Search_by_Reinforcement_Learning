import numpy as np
from mp.mp import mp
from sa.m import m
from z1.tr_online.tr_no import tr_no
np.set_printoptions(precision=3)

eid = [116, 27, 264, 184, 217, 49, 119, 175, 112, 180, 131, 93, 101, 245, 100, 33, 69, 68, 6, 129, 98, 233, 209]
s = []
for i in eid:
	m.seq_n = 1
	tr_ = tr_no(mp(i))

	s_ = tr_.run()
	s.append(s_)
	tr_.cl()
	print("{} {}".format(s[-1], i))

print(np.array(s).mean(axis=0).tolist())
