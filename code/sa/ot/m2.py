from sa.m import m
from tensorflow.keras import regularizers
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model

class m2(m):
    seq_n = 5
    h = 50
    fn = "m2"

    def md(self):
        x = Input((self.seq_n, self.x_n,), name="x")
        y = LSTM(self.h, return_sequences=True, dropout=0.2, kernel_regularizer=regularizers.l2(0.01))(x)
        #y = LSTM(h, return_sequences=True, dropout=0.2, recurrent_dropout=0.2)(x)
        y = Dense(self.y_n, activation='relu', kernel_regularizer=regularizers.l2(0.01))(y)

        self.m = Model(inputs=x, outputs=y)
        self.m.compile(loss='mse', optimizer="sgd")

