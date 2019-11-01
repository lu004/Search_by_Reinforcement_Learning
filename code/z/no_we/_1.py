import os
import numpy as np
from d.d import d
from z.no_we.m3 import m3
dd = "/ex/z/tr_te/ot"

x = d.tr_x
y = d.tr_y
g = d.tr_g
g_ = np.array([g.c for _ in range(len(x.v))])
m_ = m3()

r1 = []
n = 10
for i in range(n):
	h = m_.m.fit({"x": x.c, "y": y.c, "g": g_}, np.ones(len(x.v)),
				  batch_size=32, epochs=10, verbose=2)
	r1.append(h.history["ls"][0])
	m_.p = os.path.join(dd, str(i)+".h5")
	m_.sv()
print(r1)
