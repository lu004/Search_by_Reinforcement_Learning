import numpy as np
import os
from d.d import d, ds
from d.t import t
from d.de import de
from d.g.wv import t_cv, to_wv
from d.ul import c_sim
from z2.ul import ndcg, ndcg_k
np.set_printoptions(precision=3)

x = t(np.load(os.path.join(ds, "t_test.npy")))
g = d.te_g

top = 500
r = []
for g_, a in zip(g.c, g.ei):
	ec = to_wv(de.to_t(g_), t_cv.v)

	s = {i: c_sim(ec, x.c2[i]) for i in range(len(x.v))}
	o = sorted(s, key=s.get, reverse=True)  # max
	s2 = (x.ei[o] == a)*1

	r_ = []
	for k in range(1,top+1):
		r_.append(ndcg_k(s2, k))

	#print("@{} {}".format(10, r_[10-1]))
	r.append(r_)
print("{}".format(np.mean(np.array(r), axis=0)[[5, 10, 60]].tolist()))
