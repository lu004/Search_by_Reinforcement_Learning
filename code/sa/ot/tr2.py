import numpy as np
from mp.a import a
from sa.ot.m2 import m2
from collections import namedtuple
np.set_printoptions(precision=3)
r = namedtuple("r", ["s", "ai", "d", "s2"])

class tr:
    seq_n = m2.seq_n
    eps = 0.2
    d_long = 0.8
    r_n = 100

    n = 5
    l_max = 500
    def __init__(self, p):
        self.p = p
        self.m = m2()
        self.m2 = m2()

    def run(self):
        re = []
        self.r = []
        for _ in range(int(self.r_n)):
            self.a_pick()

        for _ in range(self.n):
            self.p.reset()
            for l in range(self.l_max):
                if l % self.r_n == 0:
                    self.tr()
                if l % (self.r_n * 2) == 0:
                    self.m2.m = self.m.cp()
                self.a_pick()

            self.tr()
            self.r = []
            re.append(self.p.get_re())
            print("{}:{}".format(self.p.eid, re[-1]))

        #self.m.sv()
        return re


    def tr(self):
        size = len(self.r)-(self.seq_n-1)
        if size >=1:
            s_ = []
            g_ = []
            for k in np.random.choice(range(size), int(size), replace=False):
            #for k in range(len(self.r)):
                r_ = self.r[k:k + self.seq_n]
                s, ai, d, s2 = map(np.array, zip(*r_))

                s2 = np.expand_dims(s2, axis=0)
                q_a = self.m.m.predict(s2)[0]
                q_v = self.m2.m.predict(s2)[0]
                q_max = []
                for i, v in enumerate(np.argmax(q_a, axis=-1)):
                    q_max.append(q_v[i][v])
                td = d + self.d_long * np.array(q_max)

                g = np.zeros([len(r_), len(a.a)])
                for i in range(len(r_)):
                    g[i][a.m[ai[i]]] = td[i]

                s_.append(s)
                g_.append(g)
            #print(len(s_))
            self.m.m.fit(np.array(s_), np.array(g_),
                         batch_size=16, epochs=5, verbose=0)


    def a_pick(self):
        s = self.seq()

        q = self.m.m.predict(np.expand_dims(s, axis=0))[0][-1]
        pr = np.ones(len(a.a), dtype=float) * self.eps / len(a.a)
        pr[np.argmax(q)] += (1.0 - self.eps)
        ai = np.random.choice(a.a, p=pr)

        s_, ai, d, s2 = self.p.run(ai)
        if len(self.r) == self.r_n: self.r.pop(0)
        self.r.append(r(s_, ai, d, s2))

    def seq(self):
        s = np.array(self.p.s_[-self.seq_n:])
        if len(s) < self.seq_n:
            s = np.r_[np.zeros([self.seq_n-len(s), len(self.p.s.st)]), s]
        # sn = 3
        # s = np.array(self.p.s_[-sn:])
        # if len(s) < sn:
        #     s = np.r_[np.zeros([sn-len(s), len(self.p.s.st)]), s]
        return s
