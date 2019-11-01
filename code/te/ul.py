import numpy as np

def ac(s, a, top=5):
	c = 0
	for i, a_ in zip(s[0], a):
		if a_ in s[1][np.argsort(i)[::-1][:top]]:
			c += 1
	r = c/len(s[0])
	print("top {} ac:{:.3f}".format(top, r))
	return r
