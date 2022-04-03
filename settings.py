import pygame
import math

pygame.init()
screenwidth = 1024
screenheight = 768
win = pygame.display.set_mode((screenwidth, screenheight))

start_coords = (screenwidth//2, screenheight//4*3)
game_framerate = 48
menu_framerate = 8

font_huge1 = pygame.font.SysFont('comicsans', screenwidth // 10)
font_large1 = pygame.font.SysFont('comicsans', screenwidth // 20)
font_normal1 = pygame.font.SysFont('comicsans', screenwidth // 40)


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_closest_enemy(Enemies, x, y):
	dists = []
	for ene in Enemies: dists.append(get_distance(x, y, *ene.rect.center))
	if dists:
		indmin = dists.index(min(dists))
		cl_ene = Enemies[indmin]
		return cl_ene
		#return get_direction(x, y, *cl_ene.rect.center)
	return 0