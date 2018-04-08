import numpy as np
import math



class AI :
	def __init__(self, row, col, dol) :
		self.row = row
		self.col = col
		self.dol = dol

		self.INFINITY = 1000000
		self.range = 2
		self.c_range = 5
		self.depth = 3
		
		self.fi_node_count = 0
		self.se_node_count = 0
		self.th_node_count = 0
		self.fo_node_count = 0
		self.fl_node_count = 0

		self.is_two = 2
		self.is_three = 3
		self.is_four = 4

		self.non_u_m = []
		self.non_d_m = []
		self.non_r_m = []
		self.non_l_m = []
		self.non_ur_m = []
		self.non_rl_m = []
		self.non_dr_m = []
		self.non_dl_m = []

		self.non_u_e = []
		self.non_d_e = []
		self.non_r_e = []
		self.non_l_e = []
		self.non_ur_e = []
		self.non_rl_e = []
		self.non_dr_e = []
		self.non_dl_e = []

		#### Testing
		self.ss = True


	def Choice(self, state) :
		#TODO : Minimax - alpha/beta - itertive
		self.fi_node_count = 0
		self.se_node_count = 0
		self.th_node_count = 0
		self.fo_node_count = 0
		self.fv_node_count = 0

		bestScoreSofar = -self.INFINITY ## is it right???

		for move_pos in self.Possible_move_list(state, self.dol) :
			move_state = self.Make_future_state(state, (move_pos[0], move_pos[1], self.dol))

			### is it right??
			score = self.Min_move(move_state, -self.INFINITY, self.INFINITY, self.depth, move_pos)
			#print('-------')
			print(score)
			print(move_pos)

			if score > bestScoreSofar :
				bestScoreSofar = score
				bestMove = move_pos
		#print(str(self.fi_node_count) + ':' + str(self.se_node_count) + ':' + str(self.th_node_count) + ':' + str(self.fo_node_count) + ':'  + str(self.fv_node_count))
		print(bestMove)

		return bestMove[0], bestMove[1], self.dol

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

	def Min_move(self, state, alpha, beta, depth, pos) :
		a, b = alpha, beta

		if depth == 0  : #when enermy win
			#print('min Score')
			if depth == 4 :
				self.fi_node_count += 1
			if depth == 3 :
				self.se_node_count += 1
			if depth == 2 :
				self.th_node_count += 1
			if depth == 1 :
				self.fo_node_count += 1

			self.fl_node_count +=1

			#print('end_min')
			#print(self.Scoring(state, (pos[0], pos[1], self.dol)))

			return self.Scoring(state)

		else :
			if depth == 4 :
				self.fi_node_count += 1
			if depth == 3 :
				self.se_node_count += 1
			if depth == 2 :
				self.th_node_count += 1
			if depth == 1 :
				self.fo_node_count += 1

			score = self.INFINITY
			for move_pos in self.Possible_move_list(state, -self.dol) :
				move_state = self.Make_future_state(state, (move_pos[0], move_pos[1], -self.dol))

				new_score = self.Max_move(move_state, a, b, depth-1, move_pos)
				b = min((b, new_score))
				#print(str(a) + ":" +str(b))

				#print(state)

				#print('choice_min')
				#print(score)

				if score > new_score :
					score = new_score
				if b <= a :
					break
			
			#print(str(self.fi_node_count) + ':' + str(self.se_node_count) + ':' + str(self.th_node_count) + ':' + str(self.fo_node_count) + ':'  + str(self.fv_node_count))

			return score

		#a, b = alpha, beta

		"""
		if win or depth end :
			return evaluateState ????
		else :
			score = self.INFINITY
			for all move(but maybe limited) :
				row, col, score = Max_move(move_state, a, b, depth - 1)
				b = Min(b, score)
				result = Min(score)
				if b <= a :
					break
			return row_result, col_result, result
		"""

	def Max_move(self, state, alpha, beta, depth, pos) :
		a, b = alpha, beta

		if depth == 0 :
			#return evaluateState() - i dont know what it is
			if depth == 4 :
				self.fi_node_count += 1
			if depth == 3 :
				self.se_node_count += 1
			if depth == 2 :
				self.th_node_count += 1
			if depth == 1 :
				self.fo_node_count += 1

			self.fl_node_count +=1
			#print('max Score')
			#print('end_max')
			#print(self.Scoring(state, (pos[0], pos[1], -self.dol)))
			return self.Scoring(state)
		else :
			if depth == 4 :
				self.fi_node_count += 1
			if depth == 3 :
				self.se_node_count += 1
			if depth == 2 :
				self.th_node_count += 1
			if depth == 1 :
				self.fo_node_count += 1
			
			#print("Node")
			score = -self.INFINITY
			for move_pos in self.Possible_move_list(state, self.dol) :
				move_state = self.Make_future_state(state, (move_pos[0], move_pos[1], self.dol))
				#if self.ss :
				#	print(move_state)

 
				new_score = self.Min_move(move_state, a, b, depth-1, move_pos)
				a = max((a, new_score))

				#print('choice_max')
				#print(score)

				if score < new_score :
					score = new_score
				if b <= a :
					#print('alpha cut off')
					break
			#print(str(self.fi_node_count) + ':' + str(self.se_node_count) + ':' + str(self.th_node_count) + ':' + str(self.fo_node_count) + ':'  + str(self.fv_node_count))

			return score

		#a, b = alpha, beta

		"""
		if win or depth end:
			return evaluateState ????
		esle :
			score = -self.INFINITY
			for all move(but maybe liimted) :
				row, col, score = Min_move(move_state, a, b, depth -1)
				a = Max(a, score)
				result = Max(score)
				if b <= a :
					break
			return row_result, col_result, result
		"""

	def Make_future_state(self, state, dol) :
		new_state = np.copy(state)

		#print(dol)
		new_state[dol[0], dol[1]] = dol[2]

		
		return new_state

	def Possible_move_list(self, state, dol) :
		possible_list = []

		## 존나 느릴것 같은데 ;;;
		for i in range(self.row) :
			for j in range(self.col) :
				if state[i, j] == dol :
					for row in range(-self.range, self.range +1) :
						for col in range(-self.range, self.range) :
							if i + row < 0 or i + row > 18 or j + col < 0 or j + col > 18:
								continue

							if state[i + row, j + col] == 0 :
								if not (i + row, j + col) in possible_list :
									possible_list.append((i + row, j + col)) 

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


	""" HURISRIC
	simple huristic
		count = 0
		score = 0
		for i in range(-self.c_range, self.c_range+1) :
			if dol[0] + i < 0 or dol[0] + i > 18:
				continue
			else :
				if state[dol[0] + i, dol[1]] == dol[2] :
					count +=1
		score = count

	advanced one 
		count = 0
		score = 0
		block = 0
		blank = 0


		for i in range(-self.c_range, self.c_range+1) :
			if dol[0] + i < 0 or dol[0] + i > 18:
				continue
			else :
				if state[dol[0] + i, dol[1]] == dol[2] :
					count +=1
					connect +=1
				if state[dol[0] + i, dol[1]] == -dol[2] :
					block +=1
					connect = 0
				if state[dol[0] + i, dol[1]] == 0 :
					blank +=1

		score = count + connect - blank - 3 * block

		if connect == 5 :
			score = self.INFINITY

		return score

	"""
	def Scoring(self, state) :
		my_score = 0
		enermy_score = 0

		for i in range(self.row) :
			for j in range(self.col) :
				if state[i, j] == self.dol :
					if (i, j) not in self.non_u :
						my_score += self.up(state, i, j, self.dol)
					if (i, j) not in self.non_d :
						my_score += self.down(state, i, j, self.dol)
					if (i, j) not in self.non_r :
						my_score += self.right(state, i, j, self.dol)
					if (i, j) not in self.non_l :
						my_score += self.left(state, i, j, self.dol)
					if (i, j) not in self.non_ur :
						my_score += self.ur(state, i, j, self.dol)
					if (i, j) not in self.non_ul :
						my_score += self.ul(state, i, j, self.dol)
					if (i, j) not in self.non_dr :
						my_score += self.dr(state, i, j, self.dol)
					if (i, j) not in self.non_dl :
						my_score += self.dl(state, i, j, self.dol)

				if state[i, j] == self.dol :
					if (i, j) not in self.non_u :
						enermy_score += self.up(state, i, j, -self.dol)
					if (i, j) not in self.non_d :
						enermy_score += self.down(state, i, j, -self.dol)
					if (i, j) not in self.non_r :
						enermy_score += self.right(state, i, j, -self.dol)
					if (i, j) not in self.non_l :
						enermy_score += self.left(state, i, j, -self.dol)
					if (i, j) not in self.non_ur :
						enermy_score += self.ur(state, i, j, -self.dol)
					if (i, j) not in self.non_ul :
						enermy_score += self.ul(state, i, j, -self.dol)
					if (i, j) not in self.non_dr :
						enermy_score += self.dr(state, i, j, -self.dol)
					if (i, j) not in self.non_dl :
						enermy_score += self.dl(state, i, j, -self.dol)

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
		self.non_rl_e.clear()
		self.non_dr_e.clear()
		self.non_dl_e.clear()

		return my_score - enermy_score


	def up(self, state, i, j, dol) :
		back = state[i+1, j]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i-k, j] == 0
				blank +=1 
				if blank > 1 :
					if state[i-k+1, j] is not 0 :
						middle_blank = 1
					break
			elif state[i-k, j] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank, k)

	def down(self) :
		back = state[i-1, j]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i+k, j] == 0
				blank +=1 
				if blank > 1 :
					if state[i+(k-1), j] is not 0 :
						middle_blank = 1
					break
			elif state[i-k, j] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank, k)

	def right(self) :
		back = state[i, j-1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i, j+k] == 0
				blank +=1 
				if blank > 1 :
					if state[i, j + (k -1)] is not 0 :
						middle_blank = 1
					break
			elif state[i, j + k] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank, k)

	def left(self) :
		back = state[i, j+1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i, j-k] == 0
				blank +=1 
				if blank > 1 :
					if state[i, j - (k -1)] is not 0 :
						middle_blank = 1
					break
			elif state[i, j - k] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank)

	def ur(self) :
		back = state[i+1, j-1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i - k, j + k] == 0
				blank +=1 
				if blank > 1 :
					if state[i - (k - 1), j + (k -1)] is not 0 :
						middle_blank = 1
					break
			elif state[i - k, j + k] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank, k)

	def ul(self) :
		back = state[i+1, j+1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i - k, j - k] == 0
				blank +=1 
				if blank > 1 :
					if state[i - (k - 1), j - (k -1)] is not 0 :
						middle_blank = 1
					break
			elif state[i - k, j - k] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank, k)

	def dr(self) :
		back = state[i - 1, j-1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i + k, j + k] == 0
				blank +=1 
				if blank > 1 :
					if state[i + (k - 1), j + (k -1)] is not 0 :
						middle_blank = 1
					break
			elif state[i + k, j + k] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank, k)

	def dl(self) :
		back = state[i-1, j+1]
		blank = 0 
		mine = 0
		middle_blank = 0

		k = 1		
		while i - k < 0 :
			if state[i + k, j - k] == 0
				blank +=1 
				if blank > 1 :
					if state[i + (k - 1), j - (k -1)] is not 0 :
						middle_blank = 1
					break
			elif state[i + k, j - k] == dol :
				break
			else : 
				mine +=1
				if blank == 0 :
					non.append([i, j])
				else : 
					non_2.appand([i, j])

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

		return self.Check_point(back, blank, mine, middle_blank, k)

	def Check_point(self, back, blank, mine, middle_blank, k)
		non = []
		non_2 = []
		score = 0
		
		if mine < 2 :
			 return 0, 0

		if mine == 2 :
			if back == 0 :
				if blank > 1:
					if middle_blank == 0 :
						return 2, 2
					else :
						return 0, 2
				elif blank == 1 :
					if middle_blank == 0 :
						return 1, 0
					else :
						return 0, 0
				else : 
					return 0, 0

			elif back == -dol :
				if middle_blank == 0 and blank > 1 :
					return 1
			else :
				print('wrong_condition!! fuck!')

		if mine == 3 :
			if back == 0 :
				if blank > 1 :
					if middle_blank == 0 :
						return 4, 3
					else : 
						return 7, 3
				elif blank == 1 :
					if middle_blank == 0 :
						return 4, 3
					else :
						return 6, 3
				else :
					return 3, 3

			elif back == -dol :
				if blank > 1 :
						return 3, 3
					else : 
						return 6, 3
				else :
					return 0, 0
			else : 
				print('wrong_condition!! fuck!')

		if mine == 4 :
			if back == 0 :
				if blank > 1 :
					if middle_blank == 0 :
						return (win)
					else :
						return 33, 4

				elif blank == 1 :
					if middle_blank == 0 :
						return (win), 4

					else : 
						return 32, 4

				else :
					return 9, 4

			elif back == -dol :
				if blank > 1 :
					if middle_blank == 0 :
						return 9, 4
					else :
						return 32, 4

				elif blank == 1 :
					if middle_blank == 0 :
						return 9, 4
					else : 
						return 31, 4
				else :
					return 0, 0
			else :
				print('wrong_condition!! fuck!')

		if mine == 5 :
			if middle_blank == 0 :
				return 50000, 5
			
			if back == 0 :
				if blank > 2 :
					return 0, 0
				elif blank == 1 :
					return 0, 0
				else :
					return 0, 0
			elif back == -dol :
				if blank < 2 :
					return 0, 0


			else :
				print('wrong_condition!! fuck!')

		print('have problem')
		return 0, 0