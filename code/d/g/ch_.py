import numpy as np
import os
from d.e import e
from d.dt import dd
from d.de import de
from d.ul import v_gi, c_sim
from d.g.wv import e_cv

e_ = e(np.load(os.path.join(dd, "e2.npy")))

q = 50
qc = e_cv.v[q]

w = {}
for i, c2 in enumerate(e_.c2):
	w[i] = c_sim(qc, c2)

o = sorted(w, key=w.get, reverse=True)  # max
r = e(e_.v[o[:30]])

print("q:{}".format(de.sh_c([q])))
for i in r.c:
	print(de.sh_c(v_gi(i)))