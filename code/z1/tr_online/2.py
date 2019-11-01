import numpy as np
from mp.mp import mp
from sa.m import m
from sa.tr import tr
from z1.tr_online.tr_no import tr_no
np.set_printoptions(precision=3)

eid = [116, 27, 264, 184, 217, 49, 119, 175, 112, 180, 131, 93, 101, 245, 100, 33, 69, 68, 6, 129, 98, 233, 209]
s = []
for i in eid:
	m.seq_n = 6
	tr.eps = 0.15
	#tr_ = tr(mp(i))
	tr_ = tr_no(mp(i))

	s_ = tr_.run()
	s2 = [sum(i) for i in s_]
	s.append(s_[np.argmax(s2)])
	tr_.cl()
	print("{} {}".format(sum(s[-1]), i))


s2 = []
n = 501
for i in s:
	a = []
	for k in range(1, n+1):
		a.append(sum(i[:k]))
	s2.append(a)
print(np.array(s2).mean(axis=0).tolist())
