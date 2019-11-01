import os
import numpy as np
import te.ul2
from d.g.tf import tf
from rw.be_.ul import d, seq_x
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.backend import clear_session

class m:
    seq_n = 8
    w_n = tf.f_n
    dd = "/ex/rw/be_/m"

    def __init__(self):
        if os.path.exists(os.path.join(self.dd, "m_x.h5")):
            self.m_x = load_model(os.path.join(self.dd, "m_x.h5"))
            self.m_y = load_model(os.path.join(self.dd, "m_y.h5"))
            #self.m_x.summary()
            #self.m_y.summary()

    def tr(self):
        xd, y1d, y2d = d()

        h_dim = 50
        # train
        x = Input(shape=(None, self.w_n))
        _, h, c = LSTM(h_dim, return_state=True)(x)
        st_x = [h, c]

        y = Input(shape=(None, self.w_n+2))
        lsm2 = LSTM(h_dim, return_sequences=True, return_state=True)
        y2, _, _ = lsm2(y, initial_state=st_x)
        den = Dense(self.w_n+2, activation='softmax')
        y2 = den(y2)

        m = Model(inputs=[x, y], outputs=y2)
        m.compile(optimizer='rmsprop', loss='categorical_crossentropy')
        m.fit([xd, y1d], y2d, batch_size=32, epochs=100, verbose=2)

        # pd
        self.m_x = Model(inputs=x, outputs=st_x)
        st = [Input(shape=(h_dim,)), Input(shape=(h_dim,))]
        y2, h, c = lsm2(y, initial_state=st)
        y2 = den(y2)
        self.m_y = Model(inputs=[y] + st, outputs=[y2] + [h, c])

        self.m_x.save(os.path.join(self.dd, "m_x.h5"))
        self.m_y.save(os.path.join(self.dd, "m_y.h5"))


    def pd(self, c):
        x = seq_x(c)
        x = np.expand_dims(x, axis=0)

        st = self.m_x.predict(x)
        y = np.zeros([1, 1, self.w_n+2])
        y[0][0][-2] = 1.

        r = []
        for _ in range(self.seq_n):
            y2, h, c = self.m_y.predict([y] + st)

            i = np.argmax(y2[0][0])
            if i == self.w_n+1:
                break
            r.append(i)

            y = np.zeros([1, 1, self.w_n + 2])
            y[0][0][i] = 1.
            st = [h, c]

        r2 = np.zeros(self.w_n)
        r2[r] = 1
        return r2

    def cl(self):
        clear_session()
