import numpy as np
from mp.mp import mp
from sa.tr import tr
from sa.m import m
np.set_printoptions(precision=3)

# train
s2 = []
for i in range(1, 2):
	m.seq_n = i
	m.h = 60

	s = []
	for eid in [253, 111, 295, 301, 275, 45, 123, 255, 36, 128]:
		tr_ = tr(mp(eid))
		s_ = tr_.run()
		s.append(s_[np.argmax(np.array(s_)[:, 0])])
		print(s[-1])
		tr_.cl()

	s2.append(np.array(s).mean(axis=0))
	print("{} {}".format(s2[-1], m.seq_n))

print(s2)