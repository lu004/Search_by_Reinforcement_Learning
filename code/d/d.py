import os
import numpy as np
from d.t import t
from d.e import e
ds = "/ex/d/d_/1/ds"

class d:
	tr_x = t(np.load(os.path.join(ds, "tr.x.npy")))
	tr_y = e(np.load(os.path.join(ds, "tr.y.npy")))
	tr2_x = t(np.load(os.path.join(ds, "tr2.x.npy")))
	tr2_y = e(np.load(os.path.join(ds, "tr2.y.npy")))
	tr_g = e(np.load(os.path.join(ds, "tr.g.npy")))

	te_x = t(np.load(os.path.join(ds, "te.x.npy")))
	te_y = e(np.load(os.path.join(ds, "te.y.npy")))
	te_g = e(np.load(os.path.join(ds, "te.g.npy")))
