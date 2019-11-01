from sklearn.feature_extraction.text import TfidfVectorizer
from d.g.ul2 import nml, stpw

def tkr(text):
    return text

class tf:
    f_n = 1000

    def __init__(self):
        self.vr = TfidfVectorizer(max_features=self.f_n, tokenizer=tkr, lowercase=False)

    def md(self, ts):
        print("tf")
        self.v = self.vr.fit_transform(ts)
        return self.v

    @staticmethod
    def sim(d1, d2):
        vr = TfidfVectorizer(tokenizer=nml, stop_words=stpw, max_features=tf.f_n)
        v = vr.fit_transform([d1, d2])
        return ((v * v.T).A)[0, 1]
