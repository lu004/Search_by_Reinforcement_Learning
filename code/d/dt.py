import os
import json
import numpy as np
from d.t import t
from d.d import ds
dd = "/ex/d/d_/1"

def load_t():
	#t_ = t(np.load(os.path.join(dd, "t4.npy")))
	#t_ = t(np.load(os.path.join(ds, "t_train.npy")))
	t_ = t(np.load(os.path.join(ds, "t_test.npy")))
	print("dt {}".format(len(t_.v)))
	return t_

class dt:
	raw = json.load(open(os.path.join(dd, "t_raw.json")))
	t = load_t()
	c = json.load(open(os.path.join(dd, "t_c.json"))) # idx:w
	u = json.load(open(os.path.join(dd, "t_u.json")))

	@staticmethod
	def sh_c(i):
		return [w for i_, w in dt.c.items() if int(i_) in i]
	@staticmethod
	def sh_u(i):
		return [w for i_, w in dt.u.items() if int(i_) in i]
