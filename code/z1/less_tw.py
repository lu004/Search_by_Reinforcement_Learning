import os
import pickle
from d.dt import dt
from d.d import ds
from sklearn.model_selection import train_test_split

eid = [116, 27, 264, 184, 217, 49, 119, 175, 112, 180, 131, 93, 101, 245, 100, 33, 69, 68, 6, 129, 98, 233, 209]
rate = [0.8, 0.6, 0.4, 0.2]

r = {}
for i in eid:
	e_ = dt.t.ge(i).ti
	_, e_ = train_test_split(e_, test_size=rate)
	r[i] = e_

pickle.dump(r, open(os.path.join(ds, "t_{}".format(rate)), 'wb'))
