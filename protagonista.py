# Purpose:
#
# Author:      Rafael Klynger e Rafaela Lacerda
#
# Created:     15/08/2014
# Copyright:   (c) Rafael 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# coding: utf-8
import pygame, sys, glob
from pygame.locals import *
import protagonista

pygame.init()

h = 650
w = 1000
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Traps of The Techies')

clock = pygame.time.Clock()
player1 = protagonista.Player()

pygame.key.set_repeat(1)
		
gameLoop = True
while gameLoop:
	clock.tick(60)
	for event in pygame.event.get():
		global gameLoop
		if event.type == QUIT:
			gameLoop = False
		player1.handle(event)
	
	screen.fill((0, 0, 0))
	
	
	# Checa qual sera a animacao
	# Run
	if player1.pos == player1.velocity:
		screen.blit(player1.img_running_R, (player1.x, player1.y))
	elif player1.pos == - player1.velocity:
		screen.blit(player1.img_running_L, (player1.x, player1.y))
	# Shot
	elif player1.shot:
		player1.shot_now()
		if player1.previous_pos == player1.velocity:
			screen.blit(player1.img_shotting_R, (player1.x, player1.y))
		elif player1.previous_pos == - player1.velocity:
			screen.blit(player1.img_shotting_L, (player1.x, player1.y))
	#Stand by
	else:
		if player1.previous_pos == - player1.velocity:
			screen.blit(player1.img_stand_by_L, (player1.x, player1.y))
			
		elif player1.previous_pos == player1.velocity:
			screen.blit(player1.img_stand_by_R, (player1.x, player1.y))
			
	player1.update(player1.pos)
	pygame.display.update()

pygame.display.quit()
