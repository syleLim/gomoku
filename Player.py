import numpy as np
import math

class player :
	def __init__(self, row, col, dol) :
		self.row = row
		self.col = col
		self.dol = dol

	def Choice(self) :
		while True :
			row = input("row 좌표를 입력하시오 1 ~ 19 : ")
			col = input("col 좌표를 입력하시오 1 ~ 19 : ")

			

			if int(row) > 0 and int(row) <= self.row and int(col) > 0 and int(col) <= self.col :
				break
			else :
				print('잘못된 입력입니다.')


		return int(row)-1, int(col)-1, self.dol
		

		#Choice input or AI


		#dol = (pos[row], pos[col], self.dol)

		#return dol