import json
import numpy as np
from d.g.tf import tf
from d.g.ul2 import nml, stpw

def txt(a):
	d = []
	for i in a:
		d.append([w for w in nml(i) if not w in stpw])

	c = {}
	for i in d:
		for w in i:
			c[w] = c[w] + 1 if w in c else 1
	o = sorted(c, key=c.get, reverse=True)  # max
	top = 1000
	o = o[:top]
	d2 = []
	for i in d:
		d2.append([w for w in i if w in o])
	return d2

def tf_run(i, d):
	tf_ = tf()
	d2 = tf_.md(d).toarray()
	v = {i_: d_ for i_, d_ in zip(i, d2)}
	return tf_, v


class json_en(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(json_en, self).default(obj)
