import numpy as np
from AI_4 import AI as ai

# function for State Count

row = 19
col = 19
dol = 1
ai = ai(row, col, dol, True)

state = np.zeros((row, col), dtype=np.int32)

def Visual(state, dol) :
	for i in range(row+2) :
		for j in range(col +2) :
			if j == 0 : 
				print(' [ ', end='')
				continue
			elif j == 20 :
				print(' ] ')
				continue
			if i == 0 or i == 20 :
				print(' - ', end='')
				continue

			if state[i-1, j-1] == 0 :
				print(' * ', end='')
			elif state[i-1, j-1] == dol :
				print(' O ', end='')
			elif state[i-1, j-1] == -dol :
				print(' X ', end='')


state[7, 7] = dol
state[9, 10] = dol
state[10, 9] = dol
state[6, 12] = dol
state[12, 12] = dol


state[8, 8] = -dol
state[9, 9] = -dol
state[10, 10] = -dol
state[11, 11] = -dol

Visual(state, dol)

score = ai.Scoring(state)

print(score)


