from sa.tr import tr

class tr_no(tr):

	def run(self):
		self.r = []
		for l in range(self.l_max):
			self.a_pick()

		#return self.p.get_re()
		return [self.p.d_]
