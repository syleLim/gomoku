import numpy as np

class A :
	def __init__(self) :
		self.r = 10
		self.c = 10



	def State(self, state) :
		new_state = state
		new_state[4, 4] = 1

		return new_state

	def Main(self) :
		state = np.zeros((self.r, self.c))

		new_state = self.State(state)

		print(state)
		print(new_state)


a = A()

a.Main()