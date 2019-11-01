
class q:
	def __init__(self, c=None, u=None, l=None, z=None):
		self.c = c
		self.u = u
		self.l = l
		self.z = z

	def show(self):
		print("c:{} u:{} l:{} z:{}".format(self.c, self.u, self.l, self.z))