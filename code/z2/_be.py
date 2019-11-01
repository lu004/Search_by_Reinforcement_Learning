import numpy as np
import os
from d.d import d, ds
from d.t import t
from d.g.wv import e_cv, to_wv
from d.ul import c_sim
from rw.be_.m import m
from z2.ul import ndcg
np.set_printoptions(precision=3)

x = t(np.load(os.path.join(ds, "t_test.npy")))
g = d.te_g

m_ = m()
x2 = []
for i in x.c:
	x2.append(to_wv(m_.pd(i), e_cv.v))

top = 500
r = []
for g_, a in zip(g.c2, g.ei):
	s = {i: c_sim(g_, x2[i]) for i in range(len(x2))}
	o = sorted(s, key=s.get, reverse=True)  # max
	s2 = (x.ei[o] == a)*1

	r_ = []
	for k in range(1,top+1):
		r_.append(ndcg(s2, k))

	#print("@{} {}".format(10, r_[10-1]))
	r.append(r_)
print("{}".format(np.mean(np.array(r), axis=0)[[5, 10, 60]].tolist()))