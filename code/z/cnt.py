import numpy as np
import os
from d.t import t
from d.d import d, ds
dd = "/ex/d/d_/1"

t1 = t(np.load(os.path.join(ds, "t_train.npy")))
t2 = t(np.load(os.path.join(ds, "t_test.npy")))
t_ = t(np.r_[t1.v, t2.v])

len(t_.v)
sum(t_.ei != -1)
len(np.unique(t_.ei))-1

t2_ = t(t_.v[t_.ei != -1])
sum(t2_.rf == 1)
sum(t2_.rf == 2)

len(np.unique(d.tr_g.ei))
len(np.unique(d.te_g.ei))


from d.dt import dt
a = dt.raw
u = {}
for k,v in a.items():
	if int(k) in t_.ti:
		u[v["user"]["id_str"]] = 1
