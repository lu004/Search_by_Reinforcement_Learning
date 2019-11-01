import os
from d.d import d
from z.no_we.m3 import m3, te_sc3
from te.ul import ac
dd = "/ex/z/tr_te/ot"

x2 = d.tr2_x
y2 = d.tr2_y
g = d.tr_g
m_ = m3()

r2 = []
n = 10
for i in range(n):
	m_.m.load_weights(os.path.join(dd, str(i) + ".h5"))
	s = te_sc3(m_, x2, g)
	r2.append(ac(s, y2.ei, top=5))
print(r2)
