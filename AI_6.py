import numpy as np
import math
import time

class AI :
	def __init__(self, row, col, dol, test) :
		self.row = row
		self.col = col
		self.dol = dol

		self.INFINITY = 1000000
		self.range = 2
		self.c_range = 5
		self.depth = 0
		self.move_choice = None
		self.is_end = False
		self.start = 0
		
		self.fi_node_count = 0
		self.se_node_count = 0
		self.th_node_count = 0
		self.fo_node_count = 0
		self.fl_node_count = 0

		self.alpha_count = 0
		self.beta_count = 0

		self.is_end = False

		self.is_two = 0
		self.is_three_e = 0
		self.is_three_b = 0
		self.is_four = 0


		self.no_verti = []
		self.no_hori = []
		self.no_dr = []
		self.no_dl = []
		self.defense_score = 50

		self.test = test

	def Choice(self, state) :
		self.is_end = False

		self.start = time.time()
		self.depth = 0
		
		best_move = []
		while True 	:
			self.fi_node_count = 0
			self.se_node_count = 0
			self.th_node_count = 0
			self.fo_node_count = 0
			self.fl_node_count = 0
			
			best_score_sofar = -self.INFINITY ## is it right???
			alpha = -self.INFINITY
			beta = self.INFINITY
			self.depth  +=1
			self.move_choice = best_move

			for move_pos in self.Possible_move_list(state) :
				if time.time() - self.start > 10 or self.is_end:
					break

				move_state = self.Make_future_state(state, (move_pos[0], move_pos[1], self.dol))

				score = self.Min_move(move_state, 1, move_pos, alpha, beta)
				alpha = max((alpha, score))

				#print('Move : ' + str(move_pos) + ' / Score : ' + str(score))
				#print()

				if score > best_score_sofar :
					best_score_sofar = score
					best_move = move_pos
			
			
				if beta <= alpha :
					self.alpha_count += 1
					break

			print(str(self.fi_node_count) + ':' + str(self.se_node_count) + ':' + str(self.th_node_count) + ':' + str(self.fo_node_count) + ':'  + str(self.fl_node_count))
			print('best_move  : '+ str(best_move))
			print('alpha : ' + str(self.alpha_count))
			print('beta : '+ str(self.beta_count))

			if time.time() - self.start > 9.5 or self.is_end:
				break

		return self.move_choice[0], self.move_choice[1], self.dol


	def Min_move(self, state, depth, pos, alpha, beta) :
		if time.time() - self.start > 9.5 :
			self.is_end = True
			return 0

		score = self.Scoring(state)

		if depth >= self.depth or score[1]: #when enermy win
			if depth == 1 :
				self.fi_node_count += 1
			if depth == 2 :
				self.se_node_count += 1
			if depth == 3 :
				self.th_node_count += 1
			if depth == 4 :
				self.fo_node_count += 1

			return score[0]

		else :
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
		if time.time() - self.start > 9.5 :
			self.is_end = True
			return 0

		score = self.Scoring(state)

		if depth >= self.depth or score[1]: 
			#return evaluateState() - i dont know what it is
			if depth == 1 :
				self.fi_node_count += 1
			if depth == 2 :
				self.se_node_count += 1
			if depth == 3 :
				self.th_node_count += 1
			if depth == 4 :
				self.fo_node_count += 1

			return score[0]
		else :

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
					for k in range(1, self.range + 1) :
						if i + k < self.row :
							if state[i + k, j] == 0 :
								if not (i+k, j) in possible_list :
									possible_list.append((i+k, j))
						if i - k >= 0 : 
							if state[i - k, j] == 0 :
								if not (i-k, j) in possible_list :
									possible_list.append((i-k, j))
						if j + k < self.col :
							if state[i, j+k] == 0 :
								if not (i, j+k) in possible_list :
									possible_list.append((i, j+k))
						if j - k >= 0 : 
							if state[i, j-k] == 0 :
								if not (i, j-k) in possible_list :
									possible_list.append((i, j-k))
						if i + k < self.row and j + k < self.col :
							if state[i+k, j+k] == 0 :
								if not (i+k, j+k) in possible_list :
									possible_list.append((i+k, j+k))
						if i-k >= 0 and j+k < self.col :
							if state[i-k, j+k] == 0 :
								if not (i-k, j+k) in possible_list :
									possible_list.append((i-k, j+k))
						if i - k >= 0 and j - k >= 0 :
							if state[i-k, j-k] == 0 :
								if not (i-k, j-k) in possible_list :
									possible_list.append((i-k, j-k))
						if i + k < self.row and j - k >= 0 :
							if state[i+k, j-k] == 0 :
								if not (i+k, j-k) in possible_list :
									possible_list.append((i+k, j-k))

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

		for i in range(0, 2) :
			for j in range(0, 2) :
				if state[int(self.row/2) +i-1, int(self.col/2) + j-1] == -self.dol :
					if int(self.row/2)+i > row/2 :
						row = int(self.col/2)+i - 1
					else :
						row = int(self.col/2)+i + 1
					col = int(self.col/2)+j
					is_find = True
					break
			if is_find :
				break
		if not is_find :
			return (int(self.row/2)-1, int(self.col/2), self.dol)

		return row, col, self.dol

	def Scoring(self, state) :
		my_score = 0
		enermy_score = 0
		ve_score = 0
		ho_score = 0
		dr_score = 0
		dl_score = 0
		ve_up_score = 0
		ho_l_score = 0
		ur_score = 0
		ul_score = 0
		e_ve_score = 0
		e_ho_score = 0
		e_dr_score = 0
		e_dl_score = 0
		e_ve_up_score = 0
		e_ho_l_score = 0
		e_ur_score = 0
		e_ul_score = 0
		special_score = 0
		e_special_score = 0


		is_win = False

		for i in range(self.row) :
			for j in range(self.col) :
				self.is_two = 0
				self.is_three_b = 0
				self.is_three_e = 0
				self.is_four = 0

				if state[i, j] == self.dol :
					ve = self.Check_vertical(state, i, j, self.dol)
					ho = self.Check_horizontal(state, i, j, self.dol)
					dr = self.Check_dr(state, i, j, self.dol)
					dl = self.Check_dl(state, i, j, self.dol)
					vu = self.Check_vertical_up(state, i, j, self.dol)
					hl = self.Check_horizontal_l(state, i, j, self.dol)
					ur = self.Check_ur(state, i, j, self.dol)
					ul = self.Check_ul(state, i, j, self.dol)

					if ve[1] or ho[1] or dr[1] or dl[1] or vu[1] or hl[1] or ur[1] or ul[1]:
						is_win = True

					ve_score +=ve[0]
					ho_score +=ho[0]
					dr_score +=dr[0]
					dl_score +=dl[0]
					ve_up_score +=vu[0]
					ho_l_score +=hl[0]
					ur_score +=ur[0]
					ul_score +=ul[0]

					if self.is_three_e > 2:
						special_score -= 5000

					if self.is_four > 0:
						if self.is_three_e > 0 :
							special_score += 70
						elif self.is_three_b > 0 :
							special_score += 20

					else :
						if self.is_two > 2:
							if self.is_three_e == 1 :
								special_score += 30
							else : 
								special_score += 20
						elif self.is_two > 0 :
							if self.is_three_e > 0 :
								special_score += 15
							else :
								special_score += 5
						
				elif state[i, j] == -self.dol :
					ve = self.Check_vertical(state, i, j, -self.dol)
					ho = self.Check_horizontal(state, i, j, -self.dol)
					dr = self.Check_dr(state, i, j, -self.dol)
					dl = self.Check_dl(state, i, j, -self.dol)
					vu = self.Check_vertical_up(state, i, j, -self.dol)
					hl = self.Check_horizontal_l(state, i, j, -self.dol)
					ur = self.Check_ur(state, i, j, -self.dol)
					ul = self.Check_ul(state, i, j, -self.dol)

					#print(dl[1])
					if ve[1] or ho[1] or dr[1] or dl[1] or vu[1] or hl[1] or ur[1] or ul[1]:
						is_win = True

					e_ve_score +=ve[0]
					e_ho_score +=ho[0]
					e_dr_score +=dr[0]
					e_dl_score +=dl[0]
					e_ve_up_score += vu[0]
					e_ho_l_score += hl[0]
					e_ur_score += ur[0]
					e_ul_score += ul[0]

					if self.is_three_e > 2:
						e_special_score -= 5000

					if self.is_four > 0:
						if self.is_three_e > 0 :
							e_special_score += 70
						elif self.is_three_b > 0 :
							e_special_score += 20

					else :
						if self.is_two > 2:
							if self.is_three_e == 1 :
								e_special_score += 30
							else : 
								e_special_score += 20
						elif self.is_two > 0 :
							if self.is_three_e > 0 :
								e_special_score += 15
							else :
								e_special_score += 5

		self.no_verti = []
		self.no_hori = []
		self.no_dr = []
		self.no_dl = []
		my_score = ve_score + ho_score + dr_score + dl_score + ve_up_score + ho_l_score + ur_score + ul_score + special_score
		enermy_score = e_ve_score + e_ho_score + e_dr_score + e_dl_score + e_ve_up_score + e_ho_l_score + e_ur_score + e_ul_score + e_special_score

		if self.test :
			print('total_verti : ' +str(ve_score))
			print('total_hori : ' +str(ho_score))
			print('total_dr : ' +str(dr_score))
			print('total_dl : ' +str(dl_score))
			print('my_score : ' + str(my_score))
			print('e_total_verti : ' +str(e_ve_score))
			print('e_total_hori : ' +str(e_ho_score))
			print('e_total_dr : ' +str(e_dr_score))
			print('e_total_dl : ' +str(e_dl_score))
			print('enermy_score : ' + str(enermy_score))

		return my_score - enermy_score, is_win

	def Check_vertical(self, state, i, j, dol) :
		offense_score = 1
		defense_score = 0
		no_check = False
		is_win = False
		enermy_line = 1
		blank = 0

		if (i, j) in self.no_verti :
			return offense_score, is_win

		for k in range(1, 5) :
			if i +k  >= self.row : break

			if state[i + k, j] == dol :
				offense_score = 2*(offense_score+1)
				if not no_check :
					self.no_verti.append((i+k, j))

				if offense_score > 22 :
					offense_score = offense_score +200
					is_win = True
			elif state[i + k, j] == -dol:

				if k == 1 :
					for x in range(1, 5) :
						if i+k+x >= self.row :
							break

						if state[i + k + x, j] == -dol :
							enermy_line +=1
							if enermy_line == 3 :
								if i + k + x + 1 >= self.row :
									break

								if state[i + k + x + 1, j] != dol :
									defense_score = self.defense_score
								else :
									break

				for x in range(1, k) :
					self.no_verti.append((i+x, j))

				if i-1 < 0  :
					offense_score = 0
					break
				
				if state[i-1, j] == -dol :
					offense_score = 0
					break
				elif state[i-1, j] == 0 :
					offense_score = offense_score/2
					break
				else :
					break
			else :
				if offense_score == 1 :
					blank +=1

				no_check = True
				continue

		if i-1 < 0  :
			return offense_score/2+defense_score, is_win

		if state[i-1, j] == -dol :
			if offense_score == 10:
				self.is_three_b +=1
			elif offense_score == 22:
				self.is_four +=1

			return offense_score/2 + defense_score, is_win
		else :
			if offense_score == 4 and blank < 2:
				self.is_two += 1
			elif offense_score == 5:
				self.is_three_b +=1
			elif offense_score == 10:
				self.is_three_e +=1
			elif offense_score == 11:
				self.is_four +=1
			elif offense_score == 22:
				self.is_four +=1

			return offense_score + defense_score, is_win

	def Check_horizontal(self, state, i, j, dol) :
		offense_score = 1
		defense_score = 0
		no_check = False
		is_win = False
		enermy_line = 1
		blank = 0

		if (i, j) in self.no_hori :
			return offense_score, is_win

		for k in range(1, 5) :
			if j + k >= self.col : break

			if state[i, j+k] == dol :
				offense_score = 2*(offense_score+1)
				if not no_check :
					self.no_hori.append((i, j+k))

				if offense_score > 22 :
					offense_score = offense_score +200
					is_win = True
			elif state[i, j + k] == -dol:
				
				if k == 1 :
					for x in range(1, 5) :
						if j+k+x >= self.col :
							break

						if state[i , j+ k + x] == -dol :
							enermy_line +=1
							if enermy_line == 3 :
								if j+ k + x + 1 >= self.col :
									break

								if state[i , j+ k + x + 1] != dol :
									defense_score = self.defense_score
								else :
									break

				for x in range(1, k) :
					self.no_hori.append((i, j+x))

				if j-1 < 0  :
					offense_score = 0
					break

				if state[i, j-1] == -dol :
					offense_score = 0
					break
				elif state[i, j-1] == 0 :
					offense_score = offense_score/2
					break
				else :
					break
			else :
				if offense_score == 1 :
					blank +=1
				no_check = True
				continue

		if  j-1 <0 :
			return offense_score/2+defense_score, is_win

		if state[i, j-1] == -dol :
			if offense_score == 10:
				self.is_three_b +=1
			elif offense_score == 22:
				self.is_four +=1
				
			return offense_score/2 + defense_score, is_win
		else :
			if offense_score == 4 and blank < 2 :
				self.is_two += 1
			elif offense_score == 5:
				self.is_three_b +=1
			elif offense_score == 10:
				self.is_three_e +=1
			elif offense_score == 11:
				self.is_four +=1
			elif offense_score == 22:
				self.is_four +=1

			return offense_score + defense_score, is_win

	def Check_dr(self, state, i, j, dol) :
		offense_score = 1
		defense_score = 0
		no_check = False
		is_win = False
		enermy_line = 1
		blank = 0

		if (i, j) in self.no_dr :
			return offense_score, is_win

		for k in range(1, 5) :
			if i + k >= self.row or j + k >= self.col : break

			if state[i + k, j +k] == dol :
				offense_score = 2*(offense_score+1)
				if not no_check :
					self.no_dr.append((i+k, j+k))
				if offense_score > 22  :
					offense_score = offense_score+200
					is_win = True
			elif state[i + k, j + k] == -dol :
				for x in range(1, 5) :
					if k == 1 :
						if i+k+x >= self.row or j+k+x >= self.col :
							break

						if state[i +k +x, j+ k + x] == -dol :
							enermy_line +=1
							if enermy_line == 3 :
								if i + k+ x + 1 >= self.row or j + k+ x + 1 >= self.col :
									break

								if state[i+ k + x + 1 , j+ k + x + 1] != dol :
									defense_score = self.defense_score
								else :
									break

				for x in range(1, k) :
					self.no_dr.append((i+x, j+ x))

				if i-1 < 0 or j-1 < 0 :
					offense_score = 0
					break

				if state[i-1, j-1] == -dol:
					offense_score = 0
					break
				elif state[i-1,j-1] == 0 :
					offense_score = offense_score/2
				else :
					break
			else :
				if offense_score == 1 :
					blank +=1
				no_check = True
				continue

		if i-1 < 0 or j-1 < 0 :
			return offense_score/2+defense_score, is_win

		if state[i-1, j-1] == -dol :
			if offense_score == 10:
				self.is_three_b +=1
			elif offense_score == 22:
				self.is_four +=1
				
			return offense_score/2 + defense_score, is_win
		else :
			if offense_score == 4 and blank < 2:
				self.is_two += 1
			elif offense_score == 5:
				self.is_three_b +=1
			elif offense_score == 10:
				self.is_three_e +=1
			elif offense_score == 11:
				self.is_four +=1
			elif offense_score == 22:
				self.is_four +=1

			return offense_score + defense_score, is_win

	def Check_dl(self, state, i, j, dol) :
		offense_score = 1
		defense_score = 0
		no_check = False
		is_win = False
		enermy_line = 1
		blank = 0

		if (i, j) in self.no_dl :
			return offense_score, is_win

		for k in range(1, 5) :
			if i + k >= self.row or j - k < 0 : break

			if state[i+k, j-k] == dol :
				offense_score = 2*(offense_score+1)
				if not no_check :
					self.no_dl.append((i+k, j-k))

				if offense_score >22:
					offense_score = offense_score  +200
					is_win = True
			elif state[i+k, j-k] == -dol :
				if k == 1 :
					for x in range(1, 5) :
						if i+k+x >= self.row or j-k-x < 0 :
							break

						if state[i+k +x, j- k - x] == -dol :
							enermy_line +=1
							if enermy_line == 3 :
								if i+k+x+1 >= self.row or j-k-x-1 < 0 :
									break

								if state[i+ k + x + 1 , j- k - x - 1] != dol :
									defense_score = self.defense_score
								else :
									break

				for x in range(1, k) :
					self.no_dl.append((i+x, j-x))

				if i-1 < 0 or j+1 >= self.col :
					offense_score = 0
					break

				if state[i-1, j+1] == -dol :
					offense_score = 0
					break
				elif state[i-1, j+1] == 0 :
					offense_score = offense_score/2
					break
				else :
					break

			else :
				if offense_score == 1 :
					blank +=1
				no_check = True
				continue

		if i-1 < 0 or j+1 >= self.col :
			return offense_score/2+defense_score, is_win

		if state[i-1, j+1] == -dol :
			if offense_score == 10:
				self.is_three_b +=1
			elif offense_score == 22:
				self.is_four +=1
				
			return offense_score/2 + defense_score, is_win
		else :
			if offense_score == 4 and blank < 2:
				self.is_two += 1
			elif offense_score == 5:
				self.is_three_b +=1
			elif offense_score == 10:
				self.is_three_e +=1
			elif offense_score == 11:
				self.is_four +=1
			elif offense_score == 22:
				self.is_four +=1

			return offense_score + defense_score, is_win


	#only defense score

	def Check_vertical_up(self, state, i, j, dol) :
		defense_score = 0
		is_win = False
		enermy_check = False
		enermy_line = 1
		connect = 1 
		blank = 0

		if (i, j) in self.no_verti :
			return 0, is_win

		for k in range(1, 5) :
			if i - k <0 : break

			if state[i - k, j] == -dol :
				if k == 1 :
					enermy_check = True

				if enermy_check :
					enermy_line +=1
					if enermy_line == 3 :
						if i - k - 1 < 0 : break

						if state[i - k - 1, j] != dol :
							defense_score = self.defense_score
						else :
							break
				else :
					connect = 0
					break
			elif state[i-k, j] == dol :
				connect += 1
			else :
				if connect == 1 :
					blank +=1
				continue
		if connect == 2 :
			if blank < 2 :
				self.is_two +=1
		if connect == 3 :
			self.is_three_e +=1
		elif connect == 4 :
			self.is_four +=1
		


		return defense_score, is_win

	def Check_horizontal_l(self, state, i, j, dol) :
		defense_score = 0
		is_win = False
		enermy_check = False
		enermy_line = 1
		blank = 0
		connect = 1

		if (i, j) in self.no_hori :
			return 0, is_win

		for k in range(1, 5) :
			if j - k <0 : break

			if state[i , j - k] == -dol :
				if k == 1 :
					enermy_check = True
				
				if enermy_check :
					enermy_line +=1
					if enermy_line == 3 :
						if j - k - 1 < 0 : break

						if state[i , j- k - 1] != dol :
							defense_score = self.defense_score
						else :
							break
				else :
					connect = 0
					break
			elif state[i, j - k] == dol :
				connect += 1
			else :
				if connect == 1 :
					blank +=1
				continue
		if connect == 2 :
			if blank < 2 :
				self.is_two +=1
		if connect == 3 :
			self.is_three_e +=1
		elif connect == 4 :
			self.is_four +=1

		return defense_score, is_win

	def Check_ur(self, state, i, j, dol) :
		defense_score = 0
		is_win = False
		enermy_line = 1
		enermy_check = True
		connect = 1
		blank = 0

		if (i, j) in self.no_dl :
			return 0, is_win

		for k in range(1, 5) :
			if i - k < 0 or j + k >= self.col : break

			if state[i- k , j + k] == -dol :
				if k == 1 :
					enermy_check = True
				if enermy_check :
					enermy_line +=1
					if enermy_line == 3 :
						if i - k - 1 < 0 or j + k + 1 >= self.col: break

						if state[i - k  - 1, j + k + 1] != dol :
							defense_score = self.defense_score
						else :
							break
				else :
					connect = 0
					break
			elif state[i - k, j - k] == dol :
				connect += 1
			else :
				if connect == 1 :
					blank +=1
				continue
		if connect == 2 :
			if blank < 2 :
				self.is_two +=1
		if connect == 3 :
			self.is_three_e +=1
		elif connect == 4 :
			self.is_four +=1

		return defense_score, is_win

	def Check_ul(self, state, i, j, dol) :
		defense_score = 0
		is_win = False
		enermy_line = 1
		enermy_check = False
		connect = 1
		blank = 0

		if (i, j) in self.no_dr :
			return 0, is_win

		for k in range(1, 5) :
			if i - k < 0  or j - k < 0 : break

			if state[i - k , j - k] == -dol :
				if k == 1 :
					enermy_check = True

				if enermy_check :
					enermy_line +=1
					if enermy_line == 3 :
						if i - k - 1 < 0 or j - k - 1 < 0 : break

						if state[i - k  - 1, j - k - 1] != dol :
							defense_score = self.defense_score
						else :
							break
				else :
					connect = 0
					break 

			elif state[i, j - k] == dol :
				connect += 1
			else :
				if connect == 1 :
					blank +=1
				continue
		if connect == 2 :
			if blank < 2 :
				self.is_two +=1
		if connect == 3 :
			self.is_three_e +=1
		elif connect == 4 :
			self.is_four +=1

		return defense_score, is_win