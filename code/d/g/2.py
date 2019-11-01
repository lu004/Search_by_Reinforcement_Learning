import numpy as np
import os
from d.dt import dt, dd
from d.de import de
from d.g.wv import t_cv, t_uv, e_cv, to_wv_all

# wv:t, e
t_ = dt.t
t_.c2_(to_wv_all(t_.c, t_cv.v))
t_.u2_(to_wv_all(t_.u, t_uv.v))
e_ = de.e
e_.c2_(to_wv_all(e_.c, e_cv.v))
np.save(os.path.join(dd, "t2"), t_.v)
np.save(os.path.join(dd, "e2"), e_.v)