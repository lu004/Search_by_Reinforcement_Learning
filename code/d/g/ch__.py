import numpy as np
import os
from d.t import t
from d.dt import dt, dd
from d.ul import v_gi, c_sim, u_sim, l_sim, z_sim
from d.g.wv import t_cv, t_uv

t_ = t(np.load(os.path.join(dd, "t4.npy")))

q = 65
qc = t_cv.v[q]
qu = t_uv.v[q]
ql = np.zeros(2)
qz = np.zeros(1)


# c
w = {}
for i, (c2, u2, l, z) in enumerate(zip(t_.c2, t_.u2, t_.l, t_.z)):
	# w[i] = c_sim(qc, c2) + \
	# 	   u_sim(qu, u2) + \
	# 	   l_sim(ql, l) + \
	# 	   z_sim(qz, z)
	w[i] = c_sim(qc, c2)
	#w[i] = u_sim(qu, u2)
	# w[i] = l_sim(ql, l)
	# w[i] = z_sim(qz, z)

o = sorted(w, key=w.get, reverse=True)  # max
r = t(t_.v[o[:30]])


print("q_c:{}".format(dt.sh_c([q])))
for i in r.c:
	print(dt.sh_c(v_gi(i)))



# u
w = {}
for i, (c2, u2, l, z) in enumerate(zip(t_.c2, t_.u2, t_.l, t_.z)):
	w[i] = u_sim(qu, u2)

o = sorted(w, key=w.get, reverse=True)  # max
r = t(t_.v[o[:30]])

print("\nq_u:{}".format(dt.sh_u([q])))
for i in r.u:
	print(dt.sh_u(v_gi(i)))
