import numpy as np
import math
import time

class AI :
	def __init__(self, row, col, dol) :
		self.row = row
		self.col = col
		self.dol = dol

		self.INFINITY = 1000000
		self.range = 1
		self.c_range = 5
		self.depth = 0
		self.move_choice = None
		self.is_end = False
		self.start = 0

		self.is_haveTo = False
		
		self.fi_node_count = 0
		self.se_node_count = 0
		self.th_node_count = 0
		self.fo_node_count = 0
		self.fl_node_count = 0

		self.alpha_count = 0
		self.beta_count = 0

		self.is_end = False


	def Choice(self, state) :
		self.is_end = False

		self.start = time.time()
		self.depth = 0
		
		bestMove = []
		while True 	:
			bestScoreSofar = -self.INFINITY ## is it right???
			alpha = -self.INFINITY
			beta = self.INFINITY
			self.depth  +=1
			self.move_choice = bestMove

			for move_pos in self.Possible_move_list(state) :
				if time.time() - self.start > 10 or self.is_end:
					break

				move_state = self.Make_future_state(state, (move_pos[0], move_pos[1], self.dol))

				temp = self.have_To(state, (move_pos[0], move_pos[1], self.dol))
			
				if  temp[0] :
					if temp[1] :
						print('must defense!')
						bestMove = temp[1]
						break
					else :
						print('must attack!')
						bestMove = move_pos
						break

				### is it right??
				score = self.Min_move(move_state, 1, move_pos, alpha, beta)
				alpha = max((alpha, score))

				print('Move : ' + str(move_pos) + ' / Score : ' + str(score))
				print()

				if score > bestScoreSofar :
					bestScoreSofar = score
					bestMove = move_pos
			
				if beta <= alpha :
					self.alpha_count += 1
					break

			print(str(self.fi_node_count) + ':' + str(self.se_node_count) + ':' + str(self.th_node_count) + ':' + str(self.fo_node_count) + ':'  + str(self.fv_node_count))
			print('best_move  : '+ str(bestMove))
			print('alpha : ' + str(self.alpha_count))
			print('beta : '+ str(self.beta_count))

			if time.time() - self.start > 10 or self.is_end:
				break

		return self.move_choice[0], self.move_choice[1], self.dol

		"""
		for all move(but maybe limited) :
			move_state = Make_future_state(a)
			row, col, score = Min_move(move_state)

			if score > bestScoreSofar (= ????) :
				bestScoreSofar = score (how to initial bestScoreSofar???)
				bestMove = (x, y)

			return bestMove

			....continue
		"""

		#dol = (pos[row], pos[col], self.dol)

		#return dol

	def Min_move(self, state, depth, pos, alpha, beta) :

		if depth >= self.depth : #when enermy win
			if depth == 1 :
				self.fi_node_count += 1
			if depth == 2 :
				self.se_node_count += 1
			if depth == 3 :
				self.th_node_count += 1
			if depth == 4 :
				self.fo_node_count += 1

			self.fl_node_count +=1

			return self.Scoring(state)

		else :
			if time.time() - self.start > 10 :
				self.is_end = True
				return 0
			if depth == 1 :
				self.fi_node_count += 1
			if depth == 2 :
				self.se_node_count += 1
			if depth == 3 :
				self.th_node_count += 1
			if depth == 4 :
				self.fo_node_count += 1

			score = self.INFINITY
			for move_pos in self.Possible_move_list(state) :
				move_state = self.Make_future_state(state, (move_pos[0], move_pos[1], -self.dol))

				new_score = self.Max_move(move_state, depth+1, move_pos, alpha, beta)
				beta = min((beta, new_score))

				if score > new_score :
					score = new_score
				
				if beta <= alpha :
					self.beta_count +=1
					break
				#print(alpha)
			
			#print(str(self.fi_node_count) + ':' + str(self.se_node_count) + ':' + str(self.th_node_count) + ':' + str(self.fo_node_count) + ':'  + str(self.fv_node_count))

			return score


	def Max_move(self, state,  depth, pos, alpha, beta) :

		if depth >= self.depth : 
			#return evaluateState() - i dont know what it is
			if depth == 1 :
				self.fi_node_count += 1
			if depth == 2 :
				self.se_node_count += 1
			if depth == 3 :
				self.th_node_count += 1
			if depth == 4 :
				self.fo_node_count += 1

			self.fl_node_count +=1

			return self.Scoring(state)
		else :
			if time.time() - self.start > 10 :
				self.is_end = True
				return 0

			if depth == 1 :
				self.fi_node_count += 1
			if depth == 2 :
				self.se_node_count += 1
			if depth == 3 :
				self.th_node_count += 1
			if depth == 4 :
				self.fo_node_count += 1
			
			score = -self.INFINITY
			for move_pos in self.Possible_move_list(state) :
				move_state = self.Make_future_state(state, (move_pos[0], move_pos[1], self.dol))

				new_score = self.Min_move(move_state, depth+1, move_pos, alpha, beta) 
				alpha = max((alpha, new_score))
				#print(beta)

				if score < new_score :
					score = new_score
				if beta <= alpha :
					self.alpha_count += 1
					break

			return score



	def Make_future_state(self, state, dol) :
		new_state = np.copy(state)

		new_state[dol[0], dol[1]] = dol[2]

		return new_state

	def Possible_move_list(self, state) :
		possible_list = []

		## 존나 느릴것 같은데 ;;;
		for i in range(self.row) :
			for j in range(self.col) :
				if state[i, j] != 0 :
					for row in range(-self.range, self.range + 1) :
						for col in range(-self.range, self.range + 1) :
							if i + row < 0 or i + row > 18 or j + col < 0 or j + col > 18:
								continue
							
							if state[i + row,  j + col] == 0 :
								if not (i + row , j + col) in possible_list :
							 		possible_list.append((i + row, j+ col))


							# if state[i,  j + col] == 0 :
							# 	if not (i , j + col) in possible_list :
							# 		possible_list.append((i, j+ col))

							# if state[i+row, col] == 0 :
							# 	if not (i + row, j) in possible_list :
							# 		possible_list.append((i+row,  j )) 


		return possible_list


	def First_choice(self, state) :
		if state[int(self.row/2), int(self.col/2)] is not 0 :
			return (int(self.row/2)-1, int(self.col/2), self.dol)
		else : 
			return (int(self.row/2), int(self.col/2), self.dol)


	def Second_choice(self, state) :
		is_find = False
		row = 0
		col = 0

		for i in range(self.row) :
			for j in range(self.col) :
				if state[i, j] == -self.dol :
					if i > row/2 :
						row = i - 1
					else :
						row = i + 1
					col = j
					is_find = True
					break
			if is_find :
				break

		return row, col, self.dol

	def Scoring(self, state) :
		pass