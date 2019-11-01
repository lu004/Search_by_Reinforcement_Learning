import numpy as np
import pickle
import os
from d.dt import dt, load_t
from d.t import t
from d.d import ds

def less_t(ei, rate):
	r = pickle.load(open(os.path.join(ds, "t_{}".format(rate)), 'rb'))

	dt.t = load_t()
	e_ = dt.t.ge(ei).gt(r[ei]).v
	v = dt.t.v[np.isin(dt.t.ei, ei, invert=True)]
	dt.t = t(np.r_[v, e_])
	print("dt {}".format(len(dt.t.v)))
