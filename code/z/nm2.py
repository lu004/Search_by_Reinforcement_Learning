import numpy as np
from d.dt import dt
from sklearn.model_selection import train_test_split

o = np.unique(dt.t.ei)
_, o2 = train_test_split(o, test_size=10)  # tr
o2 = [int(i) for i in o2]
print(o2)