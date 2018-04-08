import numpy as np
import math


class game :
	def __init__(self, row, col, black) :
		self.row = row
		self.col = col
		self.board = np.zeros((row, col), dtype = np.int32)

		self.first = black
		self.second = -black

		self.is_start = False
		self.is_end = False
		self.winner = 0

	def Update(self, dol) :
		if self.Check_correct(dol) :
			self.board[dol[0], dol[1]] = dol[2]
			
			is_win, dol_color = self.Check_win(dol)
			if  is_win :
				if dol_color == self.first :
					print('Winning dol BLACK!!')
				else :
					print('Winning dol WHITE!!')

			return True
		else :
			print('wrong_choice, choice again')
			return False

	def Check_win(self, dol) :
		if self.Check_ur(dol) or self.Check_ul(dol) or self.Check_row(dol) or self.Check_col(dol) :
			return True, dol[2]
		else :
			return False, 0
		

	def Check_correct(self, dol) :
		if self.board[dol[0], dol[1]] == 0 :
			return True
		else :
			return False

	def Visual(self) :
		for i in range(self.row+2) :
			for j in range(self.col +2) :
				if j == 0 : 
					print(' [ ', end='')
					continue
				elif j == 20 :
					print(' ] ')
					continue

				if i == 0 or i == 20 :
					print(' - ', end='')
					continue

				if self.board[i-1, j-1] == 0 :
					print(' * ', end='')
				elif self.board[i-1, j-1] == self.second :
					print(' O ', end='')
				elif self.board[i-1, j-1] == self.first :
					print(' X ', end='')

	def Check_row(self, dol) :
		connet = 0

		for i in range(-4, 5) :
			if dol[0] + i < 0 or dol[0] + i >= self.row :
				break

			if self.board[dol[0] + i , dol[1]] == dol[2] :
				connet +=1
			else :
				connet = 0

			if connet >= 5 :
				return True
		return False

	def Check_col(self, dol) :
		connet = 0

		for i in range(-4, 5) :
			if dol[1] +i < 0 or dol[1] + i >= self.col :
				break

			if self.board[dol[0], dol[1] + i] == dol[2] :
				connet +=1
			else :
				connet = 0

			if connet >= 5 :
				return True
		return False

	def Check_ur(self, dol) :
		connet = 0

		for i in range(-4, 5) :
			if dol[0] - i < 0 or dol[0] - i >= self.row or dol[1] + i < 0 or dol[1] + i >=self.col :
				break

			if self.board[dol[0] - i , dol[1] + i] == dol[2] :
				connet +=1
			else :
				connet = 0

			if connet >= 5 :
				return True
		return False

	def Check_ul(self, dol) :
		connet = 0

		for i in range(-4, 5) :
			if dol[0] + i < 0 or dol[0] + i >= self.row or dol[1] + i < 0 or dol[1] + i >=self.col :
				break

			if self.board[dol[0] + i , dol[1] + i] == dol[2] :
				connet +=1
			else :
				connet = 0

			if connet >= 5 :
				return True
		return False