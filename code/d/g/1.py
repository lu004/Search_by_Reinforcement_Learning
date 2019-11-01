import json
import os
import numpy as np
from d.dt import dt
from d.de import de
from d.g.ul import txt, tf_run, json_en
from gensim.models import Word2Vec

#dd = "/ex/d/d_/1"

# c
i, a = [], []
for k, v in dt.raw.items():
	i.append(int(k))
	a.append(v["text"])
d_c = txt(a)
tf_, c = tf_run(i, d_c)
t_c = {str(v): k for k, v in tf_.vr.vocabulary_.items()}
json.dump(t_c, open(os.path.join(dd, "t_c.json"), "w"), cls=json_en)

# u
i, a = [], []
for k, v in dt.raw.items():
	i.append(int(k))
	a.append(v["user"]["description"])
d_u = txt(a)
tf_, u = tf_run(i, d_u)
t_u = {str(v): k for k, v in tf_.vr.vocabulary_.items()}
json.dump(t_u, open(os.path.join(dd, "t_u.json"), "w"), cls=json_en)

# t
rf = {"e": 1, "i": 2, None: -1}
r = []
for v in dt.raw.values():
	t = int(v["tid"])
	e = int(v["eid"]) if v["eid"] else -1
	rf_ = rf[v["ref"]]
	if c[t].max() > 0.0:
		r.append(np.r_[t, e, rf_, c[t], u[t]])
np.save(os.path.join(dd, "t"), np.array(r))

# e
i, a = [], []
for k, v in de.raw.items():
	i.append(int(k))
	a.append(v["text"])
d_e = txt(a)
tf_, e = tf_run(i, d_e)
e_c = {str(v): k for k, v in tf_.vr.vocabulary_.items()}
json.dump(e_c, open(os.path.join(dd, "e_c.json"), "w"), cls=json_en)

r = []
for v in de.raw.values():
	i = int(v["eid"])
	if e[i].max() > 0.0:
		r.append(np.r_[i, e[i]])
np.save(os.path.join(dd, "e"), np.array(r))


# wv
def w2v(d, w_map, size=100):
	m = Word2Vec(d, size=size, min_count=1, window=50, iter=1000)
	v = np.zeros((len(w_map), size))
	for i, w in w_map.items():
		v[int(i)] = m.wv[w]
	return v

t_cv = w2v(d_c, t_c, size=274)
np.save(os.path.join(dd, "t_cv"), t_cv)

t_uv = w2v(d_u, t_u, size=321)
np.save(os.path.join(dd, "t_uv"), t_uv)

e_cv = w2v(d_e, e_c, size=204)
np.save(os.path.join(dd, "e_cv"), e_cv)
