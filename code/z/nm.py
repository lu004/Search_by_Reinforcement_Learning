import numpy as np
from d.dt import dt

c = {}
for i in np.unique(dt.t.ei):
	c[int(i)] = len(dt.t.ge(i).v)
o = sorted(c, key=c.get, reverse=True) # max
for i in o:
	print("{} {}".format(int(i), c[i]))
print(o)
print(o[:4] + o[-4:])
print(o[1:5] + o[-4:])
