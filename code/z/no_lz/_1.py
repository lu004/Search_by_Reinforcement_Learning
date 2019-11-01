import os
import numpy as np
from d.d import d
from z.no_lz.m2 import m2
dd = "/ex/z/tr_te/no_lz"

x = d.tr_x
y = d.tr_y
g = d.tr_g
g_ = np.array([g.c2 for _ in range(len(x.v))])
m_ = m2()

r1 = []
n = 10
for i in range(n):
	h = m_.m.fit({"x": x.c2, "y": y.c2, "g": g_}, np.ones(len(x.v)),
				  batch_size=32, epochs=10, verbose=2)
	r1.append(h.history["ls"][0])
	m_.p = os.path.join(dd, "{}.h5".format(i))
	m_.sv()
print(r1)
