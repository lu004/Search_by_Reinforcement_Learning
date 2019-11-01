import os
from d.d import d
from z.no_lz.m2 import m2, te_sc2
from te.ul import ac
dd = "/ex/z/tr_te/no_lz"

x2 = d.tr2_x
y2 = d.tr2_y
g = d.tr_g
m_ = m2()

r2 = []
n = 10
for i in range(n):
	m_.m.load_weights(os.path.join(dd, "{}.h5".format(i)))
	s = te_sc2(m_, x2, g)
	r2.append(ac(s, y2.ei, top=5))
print(r2)
