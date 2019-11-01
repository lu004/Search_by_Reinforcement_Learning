import numpy as np
import os
import json
from d.dt import dt, dd
from sklearn.preprocessing import scale

loc = json.load(open(os.path.join(dd, 'loc.json')))

l = []
for i in dt.t.ti:
	a = dt.raw[str(int(i))]

	done = False
	if a["place"]:
		n = a["place"]["name"].strip()
		if n in loc and loc[n]:
			l.append(loc[n])
			done = True

	if not done and a["user"]:
		n = a["user"]["location"].strip()
		if n in loc and loc[n]:
			l.append(loc[n])
		else:
			l.append(None)

l2 = [i for i in l if not i is None]
l_ = np.random.choice(range(len(l2)), len(l2), replace=False)
l_ = l_.tolist()

for i in range(len(l)):
	if l[i] is None:
		l[i] = l2[l_.pop(0)]

dt.t.l_(scale(np.array(l)))
np.save(os.path.join(dd, "t3"), dt.t.v)