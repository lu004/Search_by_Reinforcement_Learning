import numpy as np
import os
import matplotlib.pyplot as pl
from d.dt import dt, dd
from dateutil.parser import parse
from sklearn.preprocessing import scale

raw = dt.raw
# time
z = []
for i in dt.t.ti:
	a = raw[str(int(i))]
	z.append(parse(a['created_at']))

z2 = []
z_min = min(z)
for i in z:
	z2.append((i - z_min).total_seconds())
pl.hist(z2, bins=1000)
pl.show()

dt.t.z_(scale(z2))
np.save(os.path.join(dd, "t4"), dt.t.v)
