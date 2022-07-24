import pygame, sys, random
from pygame.locals import *

pygame.init()

#-----------------------GLOBAL VARIABLES------------------#
SCREEN_SIZE = (480, 640)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
grid_size = 20
clock = pygame.time.Clock()
running  = True
black = (0, 0, 0)
gray = (55, 55, 55)
white = (255, 255, 255)
origin_x, origin_y = random.randint(0, 15) * grid_size, 0
level = 250
shapes = [
			[
				[0, 0, 0],
				[0, 1, 0],
				[1, 1, 1]
			],
			[
				[0, 0, 0],
				[0, 0, 0],
				[1, 1, 1]
			],
			[
				[1, 1, 1],
				[0, 1, 0],
				[0, 0, 0]
			],
			[
				[0, 1, 0],
				[0, 1, 0],
				[0, 1, 0]
			],
			[
				[0, 0, 0],
				[1, 1, 0],
				[0, 1, 1]
			]

		]
current_shape_pos = []
select = random.randint(0, len(shapes)-1)

#-----------------------FUNCTIONS-------------------------#
def draw():
	global shapes, select, origin_x, origin_y
	o_x, o_y = origin_x, origin_y
	i = select
	for j in range(3):
		for k in range(3):
			if shapes[i][j][k] == 1:
				block = pygame.Rect(o_x, o_y, grid_size, grid_size)
				pygame.draw.rect(screen, white, block)
				current_shape_pos.append([o_x,o_y])
			o_x += grid_size
		o_x = origin_x
		o_y += grid_size
	origin_y += grid_size
	if origin_y >= SCREEN_SIZE[1]:
		origin_x, origin_y = random.randint(0, 15) * grid_size, 0
		select = random.randint(0, len(shapes)-1)

	print(origin_y)



def quit():
	pygame.quit()
	sys.exit()

def UI():
	padding_right = 120
	padding_cell = padding_right // grid_size
	next_move_box = [
						[SCREEN_SIZE[0]-padding_right, 20],
						[SCREEN_SIZE[0]-1, 20],
						[SCREEN_SIZE[0]-1, 140],
						[SCREEN_SIZE[0]-padding_right, 140]
					]

	col = SCREEN_SIZE[0] // grid_size
	row = SCREEN_SIZE[1] // grid_size
	for i in range(0,row):
		pygame.draw.line(screen, gray, (0,i*grid_size), (SCREEN_SIZE[0]-padding_right, i*grid_size))
	for j in range(0, col-padding_cell+1):
		pygame.draw.line(screen, gray, (j*grid_size, 0), (j*grid_size, SCREEN_SIZE[1]))
	pygame.draw.line(screen, gray, next_move_box[0], next_move_box[1])
	pygame.draw.line(screen, gray, next_move_box[1], next_move_box[2])
	pygame.draw.line(screen, gray, next_move_box[2], next_move_box[3])
	pygame.draw.line(screen, gray, next_move_box[0], next_move_box[3])

def move():
	pass
def generate_shape():
	pass
def show_next_shape():
	pass
def score():
	pass


#-----------------------GAME LOOP-------------------------#
while True:
	screen.fill(black)
	UI()
	draw()	
	pygame.time.delay(level)
	#move()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == KEYDOWN:
			if 	event.key == K_ESCAPE:
				quit()
	pygame.display.update()
	clock.tick(60)
