import os
import numpy as np
from d.d import d
from te.m import m
dd = "/ex/z/tr_te/1"

x = d.tr_x
y = d.tr_y
g = d.tr_g
g_ = np.array([g.c2 for _ in range(len(x.v))])
m_ = m()

r1 = []
n = 200
for i in range(n):
	h = m_.m.fit({"x": x.cnt(), "y": y.c2, "g": g_}, np.ones(len(x.v)),
				  batch_size=32, epochs=1, verbose=2)
	r1.append(h.history["ls"][0])
	m_.p = os.path.join(dd, "{}.h5".format(i))
	m_.sv()
print(r1)
