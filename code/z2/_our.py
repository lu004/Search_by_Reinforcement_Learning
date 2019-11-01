import numpy as np
import os
from d.d import d, ds
from d.t import t
from te.m import m
from z2.ul import ndcg
np.set_printoptions(precision=3)

x = t(np.load(os.path.join(ds, "t_test.npy")))
g = d.te_g

top = 500
m_ = m()

tmp = np.zeros((len(x.v), m_.g_n, m_.y_n))
r = []
for g_, a in zip(g.c2, g.ei):
	g_ = np.tile(g_, (len(x.v), 1))
	s = m_.m.predict([x.cnt(), g_, tmp]).flatten()

	s2 = {k: s[k] for k in range(len(s))}
	o = sorted(s2, key=s2.get, reverse=True)  # max
	s3 = (x.ei[o] == a)*1

	r_ = []
	for k in range(1,top+1):
		r_.append(ndcg(s3, k))
	#print("@{} {}".format(10, r_[10-1]))
	r.append(r_)
print("{}".format(np.mean(np.array(r), axis=0)[[5, 10, 60]].tolist()))
