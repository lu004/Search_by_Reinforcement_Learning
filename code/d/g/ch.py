from d.dt import dt
from d.de import de
from d.ul import v_gi

# c
c = 0
for i, v in zip(dt.t.ti, dt.t.c):
	print("\n"+dt.raw[str(int(i))]["text"])
	print(dt.sh_c(v_gi(v)))
	c += 1
	if c > 200:
		break
# u
c = 0
for i, v in zip(dt.t.ti, dt.t.u):
	print("\n"+dt.raw[str(int(i))]["user"]["description"])
	print(dt.sh_u(v_gi(v)))
	c += 1
	if c > 200:
		break
# e
for i, v in zip(de.e.ei, de.e.c):
	print("\n"+de.raw[str(int(i))]["text"])
	print(de.sh_c(v_gi(v)))



# for i in tf_.vr.vocabulary_:
# 	if not i in o:
# 		print("error")

# for i in m.wv.vocab:
# 	if not i in o:
# 		print("error")