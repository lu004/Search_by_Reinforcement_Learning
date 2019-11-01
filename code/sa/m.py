import os
import te.ul2
from tensorflow.keras import regularizers
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model, clone_model
from tensorflow.keras.backend import clear_session

class m:
    seq_n = 5
    h = 60
    x_n = 10  # s
    y_n = 8  # a
    fn = "m"

    def __init__(self):
        dd = "/ex/sa/m"
        self.p = os.path.join(dd, self.fn+".h5")
        self.md()
        # if os.path.exists(self.p):
        #     self.m.load_weights(self.p)
        #     print("ld:" + self.p)
        print("seq:{} h:{}".format(self.seq_n,self.h))
        #self.m.summary()

    def md(self):
        x = Input((None, self.x_n,), name="x")
        y = LSTM(self.h, return_sequences=False, dropout=0.2, kernel_regularizer=regularizers.l2(0.01))(x)
        y = Dense(self.y_n, activation='relu', kernel_regularizer=regularizers.l2(0.01))(y)

        self.m = Model(inputs=x, outputs=y)
        self.m.compile(loss='mse', optimizer="sgd")

    def cp(self):
        return clone_model(self.m)

    def sv(self):
        self.m.save_weights(self.p)

    def cl(self):
        clear_session()
