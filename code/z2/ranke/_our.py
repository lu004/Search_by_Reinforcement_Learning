import os
from d.d import d
from te.m import m, te_sc
from z.no_lz.m2 import m2, te_sc2
from z.no_we.m3 import m3, te_sc3
from te.ul import ac

x = d.te_x
y = d.te_y
g = d.te_g

#m_ = m()
#m_ = m2()
m_ = m3()

#s = te_sc(m_, x, g)
#s = te_sc2(m_, x, g)
s = te_sc3(m_, x, g)
r = []
for k in [3, 5, 10]:
	r.append(ac(s, y.ei, top=k))
print(r)