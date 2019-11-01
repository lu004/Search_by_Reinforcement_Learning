import numpy as np
from d.dt import dt
from d.de import de
from d.g.tf import tf

seq_n = 10

def seq_x(c):
    v = []
    for i in np.argsort(c)[::-1][:seq_n]:
        if c[i] > 0.0:
            v_ = np.zeros(tf.f_n)
            v_[i] = 1
            v.append(v_)
    for _ in range(seq_n - len(v)):
        v.append(np.zeros(tf.f_n))
    return np.array(v)

def seq_y(c):
    v = []
    for i in np.argsort(c)[::-1][:seq_n]:
        if c[i] > 0.0:
            v_ = np.zeros(tf.f_n+2)
            v_[i] = 1
            v.append(v_)
    for _ in range(seq_n - len(v)):
        v.append(np.zeros(tf.f_n+2))
    return np.array(v)

def d():
    x = np.array([seq_x(i) for i in dt.t.c])

    s = np.zeros([1, tf.f_n+2]) #start
    s[0][-2] = 1
    e = np.zeros([1, tf.f_n+2]) #end
    e[0][-1] = 1
    y1 = []
    for i in dt.t.ei:
        y1.append(np.r_[s,  seq_y(de.e.ge(i).c[0])])
    y1 = np.array(y1)
    y2 = []
    for i in dt.t.ei:
        y2.append(np.r_[seq_y(de.e.ge(i).c[0]), e])
    y2 = np.array(y2)

    return x, y1, y2
