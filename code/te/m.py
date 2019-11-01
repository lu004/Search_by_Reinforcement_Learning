import numpy as np
import os
import te.ul2
from tensorflow.keras.layers import Input, Dense, Dropout, dot, subtract
from tensorflow.keras.models import Model
from tensorflow.keras.backend import maximum, sum, mean
from tensorflow.keras import regularizers

class m:
    fn = "m"
    dd = "/ex/te/m"

    def __init__(self):
        self.p = os.path.join(self.dd, self.fn+".h5")
        self.md()
        if os.path.exists(self.p):
            self.m.load_weights(self.p)
            print("ld:" + self.p)
        self.m.summary()

    def md(self):
        self.x_n = 274+3
        self.y_n = 204
        self.g_n = 85
        x = Input((self.x_n,), name="x")
        y = Input((self.y_n,), name="y")
        g = Input((self.g_n, self.y_n), name="g")

        # x
        d = Dense(int(self.y_n*1), activation='relu', kernel_regularizer=regularizers.l2(0.01))
        #d = Dense(int(self.y_n * 1), activation='relu')
        self.x2 = Dropout(0.2)(d(x))

        # y
        d2 = Dense(int(self.y_n*1), activation='relu', kernel_regularizer=regularizers.l2(0.01))
        #d2 = Dense(int(self.y_n * 1), activation='relu')
        self.y2 = Dropout(0.2)(d2(y))
        self.g2 = Dropout(0.2)(d2(g))

        c = dot([self.y2, self.x2], axes=-1, normalize=True)
        self.m = Model(inputs=[x, y, g], outputs=c)
        self.m.compile(loss=self.ls(), optimizer='sgd', metrics=[self.ls()])


    def ls(self):
        def ls(yt, yp):
            f = dot([self.y2, self.x2], axes=-1, normalize=True)
            fg = dot([self.g2, self.x2], axes=-1, normalize=True)

            r = maximum(0.0, 0.3 + subtract([fg, f]))
            r = sum(r, axis=-1)
            return mean(r) # batch
        return ls

    def sv(self):
        self.m.save_weights(self.p)


def te_sc(m, x, g):
	sc = []
	tmp = np.zeros((len(g.v), m.g_n,m.y_n))
	for v in x.cnt():
		v_ = np.tile(v, (len(g.v),1))
		sc.append(m.m.predict([v_, g.c2, tmp]).flatten())
	return np.array(sc), g.ei