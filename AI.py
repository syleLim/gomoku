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

		self.is_two = False
		self.is_three = False
		self.is_four = False

		self.is_end = False

		self.non_u_m = []
		self.non_d_m = []
		self.non_r_m = []
		self.non_l_m = []
		self.non_ur_m = []
		self.non_ul_m = []
		self.non_dr_m = []
		self.non_dl_m = []

		self.non_u_e = []
		self.non_d_e = []
		self.non_r_e = []
		self.non_l_e = []
		self.non_ur_e = []
		self.non_ul_e = []
		self.non_dr_e = []
		self.non_dl_e = []

		#### Testing
		self.ss = True
		self.i = 0


	def Choice(self, state) :
		#TODO : Minimax - alpha/beta - itertive
		self.fi_node_count = 0
		self.se_node_count = 0
		self.th_node_count = 0
		self.fo_node_count = 0
		self.fv_node_count = 0
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

		if depth >= self.depth or self.check_must(state, (pos[0], pos[1], self.dol)): #when enermy win
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

		if depth >= self.depth or self.check_must(state, (pos[0], pos[1], -self.dol)): 
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
		my_score = 0
		enermy_score = 0

		self.is_two = False
		self.is_three = False
		self.is_four = False

		for i in range(self.row) :
			for j in range(self.col) :
				if state[i, j] == self.dol :
					if [i, j] not in self.non_u_m :
						my_score += self.up(state, i, j, self.dol)
					if [i, j] not in self.non_d_m :
						my_score += self.down(state, i, j, self.dol)
					if [i, j] not in self.non_r_m :
						my_score += self.right(state, i, j, self.dol)
					if [i, j] not in self.non_l_m :
						my_score += self.left(state, i, j, self.dol)
					if [i, j] not in self.non_ur_m :
						my_score += self.ur(state, i, j, self.dol)
					if [i, j] not in self.non_ul_m :
						my_score += self.ul(state, i, j, self.dol)
					if [i, j] not in self.non_dr_m :
						my_score += self.dr(state, i, j, self.dol)
					if [i, j] not in self.non_dl_m :
						my_score += self.dl(state, i, j, self.dol)

				if state[i, j] == -self.dol :
					if [i, j] not in self.non_u_e :
						enermy_score += self.up(state, i, j, -self.dol)
					if [i, j] not in self.non_d_e :
						enermy_score += self.down(state, i, j, -self.dol)
					if [i, j] not in self.non_r_e :
						enermy_score += self.right(state, i, j, -self.dol)
					if [i, j] not in self.non_l_e :
						enermy_score += self.left(state, i, j, -self.dol)
					if [i, j] not in self.non_ur_e :
						enermy_score += self.ur(state, i, j, -self.dol)
					if [i, j] not in self.non_ul_e :
						enermy_score += self.ul(state, i, j, -self.dol)
					if [i, j] not in self.non_dr_e :
						enermy_score += self.dr(state, i, j, -self.dol)
					if [i, j] not in self.non_dl_e :
						enermy_score += self.dl(state, i, j, -self.dol)

		#print(self.non_dr_m)
		#print(self.non_dr_e)

		self.non_u_m.clear()
		self.non_d_m.clear()
		self.non_r_m.clear()
		self.non_l_m.clear()
		self.non_ur_m.clear()
		self.non_ul_m.clear()
		self.non_dr_m.clear()
		self.non_dl_m.clear()

		self.non_u_e.clear()
		self.non_d_e.clear() 
		self.non_r_e.clear()
		self.non_l_e.clear()
		self.non_ur_e.clear()
		self.non_ul_e.clear()
		self.non_dr_e.clear()
		self.non_dl_e.clear()

		return my_score - enermy_score


	def up(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i+1, j]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1
		while i - k >= 0 :
			if state[i-k, j] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i-k+1, j] != 0 :
						middle_blank = 1
					break
			elif state[i-k, j] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i - k, j])
				else : 
					non_2.append([i - k, j])

				if mine == 5 :
					break				

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_u_m.append(no)
				self.non_d_m.append(no)
			for no in non_2 :
				self.non_d_m.append(no)
		else :
			for no in non :
				self.non_u_e.append(no)
				self.non_d_e.append(no)
			for no in non_2 :
				self.non_d_e.append(no)

		return self.Check_point(back, blank, mine, middle_blank, k, dol, i, j, 'up')

	def down(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i-1, j]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i + k < self.row :
			if state[i+k, j] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i+(k-1), j] != 0 :
						middle_blank = 1
					break
			elif state[i + k, j] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i +k, j])
				else : 
					non_2.append([i + k, j])

				if mine == 5 :
					break				

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_d_m.append(no)
				self.non_u_m.append(no)
			for no in non_2 :
				self.non_u_m.append(no)
		else :
			for no in non :
				self.non_d_e.append(no)
				self.non_u_e.append(no)
			for no in non_2 :
				self.non_u_e.append(no)

		return self.Check_point(back, blank, mine, middle_blank, k, dol, i, j, 'down')

	def right(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i, j-1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while j + k < self.col :
			if state[i, j+k] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i, j + (k -1)] != 0 :
						middle_blank = 1
					break
			elif state[i, j + k] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j + k])
				else : 
					non_2.append([i, j + k])

				if mine == 5 :
					break				

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_r_m.append(no)
				self.non_l_m.append(no)
			for no in non_2 :
				self.non_l_m.append(no)
		else :
			for no in non :
				self.non_r_e.append(no)
				self.non_l_e.append(no)
			for no in non_2 :
				self.non_l_e.append(no)

		return self.Check_point(back, blank, mine + 1, middle_blank, k, dol, i, j, 'right')

	def left(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i, j+1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while j - k >= 0 :
			if state[i, j-k] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i, j - (k -1)] != 0 :
						middle_blank = 1
					break
			elif state[i, j - k] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j - k])
				else : 
					non_2.append([i, j - k])

				if mine == 5 :
					break				

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_l_m.append(no)
				self.non_r_m.append(no)
			for no in non_2 :
				self.non_r_m.append(no)
		else :
			for no in non :
				self.non_l_e.append(no)
				self.non_l_e.append(no)
			for no in non_2 :
				self.non_r_e.append(no)

		return self.Check_point(back, blank, mine + 1, middle_blank, k, dol, i, j, 'left')

	def ur(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i+1, j-1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k  >= 0 and j + k < self.col:
			if state[i - k, j + k] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i - (k - 1), j + (k -1)] != 0 :
						middle_blank = 1
					break
			elif state[i - k, j + k] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i - k , j + k])
				else : 
					non_2.append([i - k, j + k])

				if mine == 5 :
					break				

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_ur_m.append(no)
				self.non_dl_m.append(no)
			for no in non_2 :
				self.non_dl_m.append(no)
		else :
			for no in non :
				self.non_ur_e.append(no)
				self.non_dl_e.append(no)
			for no in non_2 :
				self.non_dl_e.append(no)

		return self.Check_point(back, blank, mine + 1, middle_blank, k, dol, i, j, 'ur')

	def ul(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i+1, j+1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k >= 0 and j - k >= 0 :
			if state[i - k, j - k] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i - (k - 1), j - (k -1)] != 0 :
						middle_blank = 1
					break
			elif state[i - k, j - k] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i - k, j - k])
				else : 
					non_2.append([i - k, j - k])

				if mine == 5 :
					break				

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_ul_m.append(no)
				self.non_dr_m.append(no)
			for no in non_2 :
				self.non_dr_m.append(no)
		else :
			for no in non :
				self.non_ul_e.append(no)
				self.non_dr_e.append(no)
			for no in non_2 :
				self.non_dr_e.append(no)

		return self.Check_point(back, blank, mine + 1, middle_blank, k, dol, i, j, 'ul')

	def dr(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i-1, j-1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1
		while i + k < self.row and j + k < self.col:
			if state[i + k, j + k] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i + (k - 1), j + (k -1)] != 0 :
						middle_blank = 1
					break
			elif state[i + k, j + k] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i + k, j + k])
				else : 
					non_2.append([i + k, j + k])

				#print(non)

				if mine == 5 :
					break

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_dr_m.append(no)
				self.non_ul_m.append(no)
			for no in non_2 :
				self.non_ul_m.append(no)
		else :
			for no in non :
				self.non_dr_e.append(no)
				self.non_ul_e.append(no)
			for no in non_2 :
				self.non_ul_e.append(no)

		return self.Check_point(back, blank, mine + 1, middle_blank, k, dol, i, j, 'dr')

	def dl(self, state, i, j, dol) :
		non = []
		non_2 = []
		back = state[i-1, j+1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i + k < self.col and j - k >= 0 :
			if state[i + k, j - k] == 0 :
				blank +=1 
				if blank > 1 :
					if state[i + (k - 1), j - (k -1)] != 0 :
						middle_blank = 1
					break
			elif state[i + k, j - k] == -dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i + k, j - k])
				else : 
					non_2.append([i + k, j - k])

				if mine == 5 :
					break				

			if k > 4 :
				break

			k += 1

		if dol == self.dol :
			for no in non :
				self.non_dl_m.append(no)
				self.non_ur_m.append(no)
			for no in non_2 :
				self.non_ur_m.append(no)
		else :
			for no in non :
				self.non_dl_e.append(no)
				self.non_ur_e.append(no)
			for no in non_2 :
				self.non_ur_e.append(no)

		return self.Check_point(back, blank, mine + 1, middle_blank, k, dol, i, j, 'dl')

	def Check_point(self, back, blank, mine, middle_blank, k, dol, i, j, flag) :
		non = []
		non_2 = []
		score = 0
		
		if mine < 2 :
			return 0

		if mine == 2 :
			if back == 0 :
				if blank > 1:
					if middle_blank == 0 :
						if self.is_three :
							return 20

						if self.is_two :
							return 10
						else :
							self.is_two = True
							return 2
					else :
						return 0
				elif blank == 1 :
					if middle_blank == 0 :
						return 1
					else :
						return 0
				else : 
					return 0

			elif back == -dol :
				if blank > 1 :
					if middle_blank == 0 :
						return 1
					else :
						return 0
				else :
					return 0
			else :
				if self.ss :
					print('wrong_condition!! fuck!')

		if mine == 3 :
			if back == 0 :
				if blank > 1 :
					if middle_blank == 0 :
						if self.is_four :
							return 10000

						if self.is_three :
							return 50
						else :
							self.is_three = True
							return 4
					else :
						if self.is_four :
							return 10000

						if self.is_three :
							return 50
						else :
							self.is_three = True
							return 7
				elif blank == 1 :
					if middle_blank == 0 :
						if self.is_four :
							return 100

						if self.is_three :
							return 20
						else :
							self.is_three = True
							return 4
					else :
						if self.is_four :
							return 100
						
						if self.is_three :
							return 20
						else :
							self.is_three = True
							return 6
				else :
					if self.is_four :
						return 50

					if self.is_three :
						return 20
					else :
						self.is_three = True
						return 3

			elif back == -dol :
				if blank > 1 :
					if middle_blank == 0 :
						if self.is_four :
							return 50
						else :
							return 3
					else : 
						if self.is_four :
							return 50
						else :
							return 6
				else :
					return 0
			else : 
				if self.ss :
					print('wrong_condition!! fuck!')

		if mine == 4 :
			if back == 0 :
				if blank > 1 :
					if middle_blank == 0 :
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 1000
					else :
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 33
						

				elif blank == 1 :
					if middle_blank == 0 :
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 1000
					else : 
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 32
				else :
					if self.is_four :
							return 10000
					else :
						self.is_four = True
						return 9

			elif back == -dol :
				if blank > 1 :
					if middle_blank == 0 :
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 9
					else :
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 32

				elif blank == 1 :
					if middle_blank == 0 :
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 9
					else : 
						if self.is_four :
							return 10000
						else :
							self.is_four = True
							return 31
				else :
					return 0
			else :
				print('wrong_condition!! fuck!')

		if mine == 5 :
			if middle_blank == 0 :
				return self.INFINITY
			
			if back == 0 :
				if blank > 2 :
					return 0
				elif blank == 1 :
					return 0
				else :
					return 0
			elif back == -dol :
				if blank < 2 :
					return 0
			else :
				if self.ss :
					print('wrong_condition!! fuck!')
		
		if mine == 6 :
			return -10000
		
		print('have problem : ' + flag)
		print('dr_k : ' + str(k) + '   dol : ' + str(dol) + '  i, j : ' +str(i) + ', '  + str(j))
		print('mine : ' + str(mine) + "   blank : " + str(blank) +  '   back : ' + str(back) + ' middle_blank : ' + str(middle_blank))
		
		return 0

	def check_must(self, state, dol) :
		return self.check_win_state_up(state, dol)
			

	def check_win_state_up(self, state, dol) :
		connect = 0
		#up
		for i in range(1, 5) :
			if dol[0] + i >= self.row :
				break

			if state[dol[0] + i , dol[1]] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] + i , dol[1]] == -dol[2] :
				break
			else :
				if connect == 4 :
					if state[dol[0] - 1, dol[1]] == 0 :
						return True
		connect = 0
		#down
		for i in range(1, 5) : 
			if dol[0] - i < 0 :
				break

			if state[dol[0] - i , dol[1]] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] - i , dol[1]] == -dol[2] :
				break
			else :
				if connect == 3 :
					if state[dol[0] + 1, dol[1]] == 0 :
						return True
		connect = 0
		#right
		for i in range(1, 5) : 
			if dol[1] + i >= self.col :
				break

			if state[dol[0] , dol[1] + i] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] , dol[1] + i] == -dol[2] :
				break
			else :
				if connect == 3 :
					if state[dol[0] , dol[1] -1] == 0 :
						return True
		connect = 0
		#right
		for i in range(1, 5) : 
			if dol[1] - i < 0 :
				break

			if state[dol[0] , dol[1] - i] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] , dol[1] - i] == -dol[2] :
				break
			else :
				if connect == 3 :
					if state[dol[0] , dol[1] +1] == 0 :
						return True
		connect = 0
		#ur
		for i in range(1, 5) : 
			if dol[0] - i < 0 or dol[1] + i >= self.col :
				break

			if state[dol[0] -i , dol[1] + i] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] -i , dol[1] + i] == -dol[2] :
				break
			else :
				if connect == 3 :
					if state[dol[0] +1, dol[1] -1] == 0 :
						return True
		connect = 0
		#ul
		for i in range(1, 5) : 
			if dol[0] - i < 0 or dol[1] - i < 0 :
				break
			if state[dol[0]- i , dol[1] - i] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] -i, dol[1] - i] == -dol[2] :
				break
			else :
				if connect == 3 :
					if state[dol[0] + 1 , dol[1] +1] == 0 :
						return True
		connect = 0
		#dr
		for i in range(1, 5) : 
			if dol[0] + i >= self.row or dol[1] + i >= self.col :
				break

			if state[dol[0] +i, dol[1] + i] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] +i, dol[1] + i] == -dol[2] :
				break
			else :
				if connect == 3 :
					if state[dol[0]-1 , dol[1] -1] == 0 :
						return True
		connect = 0
		#dl
		for i in range(1, 5) : 
			if dol[0] + i >= self.row or dol[1] - i < 0 :
				break

			if state[dol[0] +i, dol[1] - i] == dol[2] :
				connect += 1
				if connect == 4 :
					return True
			elif state[dol[0] +i, dol[1] - i] == -dol[2] :
				break
			else :
				if connect == 3 :
					if state[dol[0] -1, dol[1] +1] == 0 :
						return True
		return False

	def have_To(self, state, dol) :
		flag_1 = self.check_win_state_up(state, dol)
		flag_2 = self.enermy_check(state, dol)

		if flag_2[0] :
			return flag_2

		if flag_1 :
			return flag_1, None
		
		return False, None

	def enermy_check(self, state, dol) :
		blank = 0
		#up
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[0] + i >= self.row :
				break

			if state[dol[0] + i, dol[1]] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0 :
						if state[dol[0] + i + 1, dol[1]] != self.dol :
							return True, (dol[0], dol[1])
						else : 
							continue
					else :
						if state[dol[0] + i + 1, dol[1]] != self.dol :
							return True, blank_move
				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0] + i, dol[1]] == 0 :
				blank +=1
				blank_move = (dol[0] + i, dol[1])
			else :
				break

		#down
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[0] - i < 0 :
				break

			if state[dol[0] - i, dol[1]] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0 :
						if state[dol[0] - i - 1, dol[1]] != self.dol :
							return True, (dol[0], dol[1])
						else :
							continue
					else :
						if state[dol[0] - i - 1, dol[1]] != self.dol :
							return True, blank_move
				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0] - i, dol[1]] == 0 :
				blank +=1
				blank_move = (dol[0] - i , dol[1])
			else :
				break


		#right
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[0] + i > self.col :
				break

			if state[dol[0], dol[1] + i] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0 :
						if state[dol[0] , dol[1] + i + 1] != self.dol :
							return True, (dol[0], dol[1])
						else :
							continue
					else :
						if state[dol[0], dol[1] + i +1] != self.dol :
							return True, blank_move
				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0], dol[1] + i] == 0 :
				blank +=1
				blank_move = (dol[0], dol[1] + i)
			else :
				break
		

		#left
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[1] - i < 0 :
				break

			if state[dol[0], dol[1] - i] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0 :
						if state[dol[0] , dol[1] - i - 1] != self.dol :
							return True, (dol[0], dol[1])
						else :
							continue
					else : 
						if state[dol[0] , dol[1] - i - 1] != self.dol :
							return True, blank_move

				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0], dol[1] - i] == 0 :
				blank +=1
				blank_move = (dol[0], dol[1] - i)
			else :
				break

		#ur
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[0] - i < 0 or dol[1] + i >= self.col:
				break

			if state[dol[0] - i, dol[1] + i] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0:
						if state[dol[0] - i - 1 , dol[1] + i + 1] != self.dol :
							return True, (dol[0], dol[1])
						else :
							continue
					else : 
						if state[dol[0] - i - 1 , dol[1] + i + 1] != self.dol :
							return True, blank_move
				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0] - i, dol[1] + i] == 0 :
				blank +=1
				blank_move = (dol[0] - i, dol[1] + i)
			else :
				break

		#ul
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[0] - i < 0 or dol[1] - i < 0:
				break

			if state[dol[0] - i, dol[1] - i] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0:
						if state[dol[0] - i - 1 , dol[1] - i - 1] != self.dol :
							return True, (dol[0], dol[1])
						else :
							continue
					else : 
						if state[dol[0] - i - 1 , dol[1] - i - 1] != self.dol :
							return True, blank_move
				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0] - i, dol[1] - i] == 0 :
				blank +=1
				blank_move = (dol[0] - i, dol[1] - i)
			else :
				break

		#dr
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[0] + i > self.row or dol[1] + i >= self.col:
				break

			if state[dol[0] + i, dol[1] + i] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0:
						if state[dol[0] + i + 1 , dol[1] + i + 1] != self.dol :
							return True, (dol[0], dol[1])
						else :
							continue
					else : 
						if state[dol[0] + i + 1 , dol[1] + i + 1] != self.dol :
							return True, blank_move
				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0] + i, dol[1] + i] == 0 :
				blank +=1
				blank_move = (dol[0] + i, dol[1] + i)
			else :
				break

		#dl
		e_c = 0
		blank_move = None
		for i in range(1, 5) : 
			if dol[0] + i >= self.row or dol[1] - i < 0:
				break

			if state[dol[0] + i, dol[1] - i] == -self.dol :
				e_c +=1
				if e_c == 3 :
					if blank == 0:
						if state[dol[0] + i + 1 , dol[1] - i - 1] != self.dol :
							return True, (dol[0], dol[1])
						else :
							continue
					else : 
						if state[dol[0] + i + 1 , dol[1] - i - 1] != self.dol :
							return True, blank_move
				if e_c == 4 :
					return True, (dol[0], dol[1])
			elif state[dol[0] + i, dol[1] - i] == 0 :
				blank +=1
				blank_move = (dol[0] + i, dol[1] - i)
			else :
				break

		return False, None