from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.corpus import stopwords
import nltk, string

rm_pun = dict((ord(char), None) for char in string.punctuation)
stmr = nltk.stem.porter.PorterStemmer()

def nml(t):
    # remove punctuation, stem
    tk = nltk.word_tokenize(t.lower().translate(rm_pun))
    r = [stmr.stem(i) for i in tk]
    # print("\nnormalize")
    # for w in re:
    #     print(w)
    return r

lst = [
    "cnnbrk",
    '’',
    '“',
    'https…',
    'htt…',
    'h…',
    's',
    't',
    "cnnbrk…",
    "”",
    "…",
    "wo…",
    "”",
    "…",
    "w…",
    "a…",
    "m…",
    "i…",
    "t…",
    "‘",
    "an…",
    "g…",
    "d…",
    "to…",
    "p…",
    "o…",
    "is…",
    "in…",
    "wh…",
    "c…",
    "⁦…",
    "so…",
    "y…",
    "and…",
    "मे",
    "तो",
    "से",
    "be…",
    "re…",
    "are…",
    "as…",
    "no…",
    "r…",
    "ft…",
    "they…",
    "—",
    "not…",
    "f…",
    "l…",
    "e…",
    "it…",
    "u…",
    "b…",
    "n…",
    "tr…",
    "we…"
]
stpw = ENGLISH_STOP_WORDS.union(stopwords.words('english')).union(lst)
