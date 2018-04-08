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

		self.is_haveTo = False
		
		self.fi_node_count = 0
		self.se_node_count = 0
		self.th_node_count = 0
		self.fo_node_count = 0
		self.fl_node_count = 0

		self.alpha_count = 0
		self.beta_count = 0

		self.is_end = False


		self.no_verti = []
		self.no_hori = []
		self.no_dr = []
		self.no_dl = []

		self.test = test

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

			print(str(self.fi_node_count) + ':' + str(self.se_node_count) + ':' + str(self.th_node_count) + ':' + str(self.fo_node_count) + ':'  + str(self.fl_node_count))
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
					for k in range(1, self.range + 1) :
						if state[i + k, j] == 0 :
							if not (i+k, j) in possible_list :
								possible_list.append((i+k, j))
						if state[i - k, j] == 0 :
							if not (i-k, j) in possible_list :
								possible_list.append((i-k, j))
						if state[i, j+k] == 0 :
							if not (i, j+k) in possible_list :
								possible_list.append((i, j+k))
						if state[i, j-k] == 0 :
							if not (i, j-k) in possible_list :
								possible_list.append((i, j-k))
						if state[i+k, j+k] == 0 :
							if not (i+k, j+k) in possible_list :
								possible_list.append((i+k, j+k))
						if state[i-k, j+k] == 0 :
							if not (i-k, j+k) in possible_list :
								possible_list.append((i-k, j+k))
						if state[i-k, j-k] == 0 :
							if not (i-k, j-k) in possible_list :
								possible_list.append((i-k, j-k))
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
		ve_score = 0
		ho_score = 0
		dr_score = 0
		dl_score = 0
		e_ve_score = 0
		e_ho_score = 0
		e_dr_score = 0
		e_dl_score = 0

		is_win = False

		for i in range(self.row) :
			for j in range(self.col) :
				if state[i, j] == self.dol :
					ve = self.Check_vertical(state, i, j, self.dol)
					ho = self.Check_horizontal(state, i, j, self.dol)
					dr = self.Check_dr(state, i, j, self.dol)
					dl = self.Check_dl(state, i, j, self.dol)

					if ve[1] or ho[1] or dr[1] or dl[1] :
						is_win = True

					ve_score +=ve[0]
					ho_score +=ho[0]
					dr_score +=dr[0]
					dl_score +=dl[0]

				elif state[i, j] == -self.dol :
					ve = self.Check_vertical(state, i, j, -self.dol)
					ho = self.Check_horizontal(state, i, j, -self.dol)
					dr = self.Check_dr(state, i, j, -self.dol)
					dl = self.Check_dl(state, i, j, -self.dol)

					if ve[1] or ho[1] or dr[1] or dl[1] :
						is_win = True

					e_ve_score +=ve[0]
					e_ho_score +=ho[0]
					e_dr_score +=dr[0]
					e_dl_score +=dl[0]

		self.no_verti = []
		self.no_hori = []
		self.no_dr = []
		self.no_dl = []
		my_score = ve_score + ho_score + dr_score + dl_score
		enermy_score = e_ve_score + e_ho_score + e_dr_score + e_dl_score

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
			print('my_score : ' + str(e_my_score))
			print('enermy_score : ' + str(enermy_score))

		return my_score - enermy_score, is_win

	def Check_vertical(self, state, i, j, dol) :
		score = 1
		no_check = False

		if (i, j) in self.no_verti :
			return score, False
		
		for k in range(1, 5) :
			if i + k >= self.row : break

			if state[i + k, j] == dol :
				score = 2*(score+1)
				if not no_check :
					self.no_verti.append((i+k, j))

				if score > 60 :
					return score +80, True
			elif state[i + k, j] == -dol :
				for x in range(1, k) :
					self.no_verti.append((i, j+x))

				if state[i-1, j] == -dol :
					return 0, False
				elif state[i-1, j] == 0 :
					return score/2, False
				else :
					break

			else :
				no_check = True
				continue

		if state[i-1, j] == -dol :
			return score/2, False
		else :
			return score, False

	def Check_horizontal(self, state, i, j, dol) :
		score = 1
		no_check = False

		if (i, j) in self.no_hori :
			return score, False

		for k in range(1, 5) :
			if j + k >= self.col : break

			if state[i, j+k] == dol :
				score = 2*(score+1)
				if not no_check :
					self.no_hori.append((i, j+k))

				if score > 40 :
					return score+80, True
			elif state[i, j + k] == -dol:
				for x in range(1, k) :
					self.no_hori.append((i, j+x))

				if state[i, j-1] == -dol :
					return 0, False
				elif state[i, j-1] == 0 :
					return score/2, False
				else :
					break

			else :
				no_check = True
				continue

		if state[i, j-1] == -dol :
			return score/2, False
		else :
			return score, False

	def Check_dr(self, state, i, j, dol) :
		score = 1
		no_check = False		

		if (i, j) in self.no_dr :
			return score, False

		for k in range(1, 5) :
			if i + k >= self.row or j + k >= self.col : break

			if state[i + k, j +k] == dol :
				score = 2*(score+1)
				if not no_check :
					self.no_dr.append((i+k, j+k))
				if score > 40  :
					return score +80, True
			elif state[i+k, j + k] == -dol :
				for x in range(1, k) :
					self.no_dr.append((i+x, j+ x))

				if state[i-1, j-1] == -dol:
					return 0, False
				elif state[i-1,j-1] == 0 :
					return score/2, False
				else :
					break

			else :
				no_check = True
				continue

		if state[i-1, j-1] == -dol :
			return score/2, False
		else :
			return score, False

	def Check_dl(self, state, i, j, dol) :
		score = 1
		no_check = False

		if (i, j) in self.no_dl :
			return score, False

		for k in range(1, 5) :
			if i + k >= self.row or j - k < 0 : break

			if state[i+k, j-k] == dol :
				score = 2*(score+1)
				if not no_check :
					self.no_dl.append((i+k, j-k)) 

				if score >40:
					return score +80, True
			elif state[i+k, j-k] == -dol :
				for x in range(1, k) :
					self.no_dl.append((i+x, j-x))

				if state[i-1, j+1] == -dol :
					return 0, False
				elif state[i-1, j+1] == 0 :
					return score/2, False
				else :
					break

			else :
				no_check = True
				continue

		if state[i-1, j+1] == -dol :
			return score/2, False
		else :
			return score, False

 

		