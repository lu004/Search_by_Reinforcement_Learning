import os
from d.d import d
from te.m import m, te_sc
from te.ul import ac
dd = "/ex/z/tr_te/1"

x2 = d.tr2_x
y2 = d.tr2_y
g = d.tr_g
m_ = m()

r2 = []
n = 200
for i in range(n):
	if i>=100:
		m_.m.load_weights(os.path.join(dd, str(i) + ".h5"))
		s = te_sc(m_, x2, g)
		r2.append(ac(s, y2.ei, top=5))
print(r2)
