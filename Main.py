import numpy as np
import math

from game import game
from AI import AI as ai
#from AI_2 import AI as ai_2
#from AI_3 import AI as ai_3
#from AI_4 import AI as ai_4
from AI_5 import AI as ai_5
from AI_6 import AI as ai_6
from Player import player

row = 19
col = 19
white = 1
black = -white

turn_count = 0
game = game(row, col, black)

while True :
	print('모드를 선택하세요.')
	print('1. Player vs AI')
	print('2. AI vs AI')

	mode = input('입력하시오 : ')

	if mode == '1':
		break

	elif mode == '2' :
		break
	else : 
		print('잘못된 입력입니다.')
		continue

if mode == '1' :
	while True :
		print ('순서를 선택하세요.')
		print('1 : Player 선 / 2. AI 선')
		temp = input('입력하시오 : ')

		if temp == '1' :
			pl = player(row, col, black)
			ai = ai_6(row, col, white, False)
			break
		elif temp == '2' :
			pl = player(row, col, white)
			ai = ai_6(row, col, black, False)
			break
		else :
			print('잘못된 입력입니다.')
			continue
else :
	pl = ai_5(row, col, black, False)
	ai = ai_6(row, col, white, False)

# 1 = white(second) / -1 = black(first)

print('game_start')
turn_count +=1

if ai.dol == black :
	dol = ai.First_choice(game.board)
	turn_count +=1
	turn = 'pl'
else :
	if mode == '1' :
		dol = pl.Choice()
		turn_count +=1
		turn = 'ai'
	else :
		dol = pl.First_choice(game.board)
		turn_count +=1
		turn = 'ai'

game.Update(dol)

game.Visual()
	
while True :
	state = game.board

	if turn == 'ai' :
		if turn_count ==2 :
			dol = ai.Second_choice(state)

		else :
			dol = ai.Choice(state)

		turn_count +=1
		
	else : 
		if mode == '1' :
			dol = pl.Choice()
			turn_count +=1
		else :
			dol = pl.Choice(state)
			turn_count +=1

	print('dol_choice' + str(dol))

	if not game.Update(dol) :
		continue
	else :
		if turn == 'ai' :
			turn = 'pl'
		else :
			turn = 'ai'

	game.Visual()

	if game.Check_win(dol)[0] :
		break