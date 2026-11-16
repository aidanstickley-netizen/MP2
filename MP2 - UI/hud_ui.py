import pygame
import random
# frame rate is 60/s
# animation frame rate is 12/s

pygame.init()   #this will initiate pygame for your program
Screen1 = pygame.display.set_mode((800,400))    
color = (100, 100, 255)
Screen1.fill(color)

scr = pygame.image.load("graphics/scr_rotate.png")
bar = pygame.image.load("graphics/hud/hit_bar.png")
hearts = pygame.image.load("graphics/hud/hearts.png")

ui_1 = pygame.image.load("graphics/hud/equipped_item_ui.png")
ui_1 = pygame.transform.scale(ui_1, (66 * 3, 17 * 3))

numbers = pygame.image.load("graphics/hud/zero_to_nine_num_black.png")

equipment = pygame.image.load("graphics/equipment/weapons_icon.png")


def wobble(original_value, active = True):
	if active:
		return original_value + random.randint(-3, 3)
	else:
		return original_value

def mirror_image(object, check):
	if check:
		object = pygame.transform.flip(object, -1, 0)
	return object

class spriteSheet():
	def __init__(self, image):
		self.sheet = image
	def get_frame(self, frame, width, height, scale):
		individual_img = pygame.Surface((width, height), pygame.SRCALPHA)
		individual_img.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		individual_img = pygame.transform.scale(individual_img, (width * scale, height * scale))
		return individual_img


Animation_object = spriteSheet(scr)
Frames = [Animation_object.get_frame(i, 9, 9, 3) for i in range(8)]

Animation_object_bar = spriteSheet(bar)
Frames_bar = [Animation_object_bar.get_frame(i, 49, 7, 3) for i in range(8)]

Animation_object_heart = spriteSheet(hearts)
Frames_heart = [Animation_object_heart.get_frame(i, 9, 9, 3) for i in range(5)]

Animation_object = spriteSheet(numbers)
number = [Animation_object.get_frame(i, 3, 7, 3) for i in range(10)]



Animation_object = spriteSheet(equipment)
held_equipment = [Animation_object.get_frame(i, 13, 13, 3) for i in range(75)]

frame_var = 0 #placeholder
heart_level = 0 #placeholder
Game_active = True

animation_tick = 0
ticking_tool = 0

def display_num(value):
	print(value)

def make_ui(x_cord, y_cord, mirror, bar, heart):
	bar_add_x = x_cord + 12
	mirror_buff = [0, 30, 60]
	held_equipment_mirror = [6, 66, 126]

	if mirror:
		bar_add_x += 27
		mirror_buff = [120, 90, 60]
		held_equipment_mirror = [153, 93, 33]

	hearts = [0, 0, 0]
	if heart > 4:
		if heart > 8:
			hearts[0] = 4
			hearts[1] = 4
			hearts[2] = heart - 8
		else:
			hearts[0] = 4
			hearts[1] = heart - 4
	else:
		hearts[0] = heart

	Screen1.blit(mirror_image(ui_1, mirror), (x_cord, y_cord))
	Screen1.blit(mirror_image(Frames_bar[bar], mirror), (bar_add_x, y_cord + 54))

	for x in range(3):
		Screen1.blit(mirror_image(Frames_heart[hearts[x]], mirror), (bar_add_x + mirror_buff[x], y_cord + 54 + 24))

	
	Screen1.blit(mirror_image(held_equipment[4], mirror), (x_cord + held_equipment_mirror[0], y_cord + 6))
	Screen1.blit(mirror_image(held_equipment[5], mirror), (x_cord + held_equipment_mirror[1], y_cord + 6))
	Screen1.blit(mirror_image(held_equipment[6], mirror), (x_cord + held_equipment_mirror[2], y_cord + 6))
	
while Game_active:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Game_active = False
		if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						if frame_var < 7:
							frame_var +=1
						else:
							frame_var = 0
					elif event.key == pygame.K_s:
						if heart_level < 12:
							heart_level +=1
						else:
							heart_level = 0
						print(heart_level)

	Screen1.fill(color)

	Screen1.blit(Frames[animation_tick % 8], (200,200))
	Screen1.blit(number[animation_tick % 10], (300,200))

	display_num(165)

	make_ui(15, 15, False, frame_var, heart_level)
	make_ui(585, 15, True, 5, 7)
	
	pygame.display.update()
	pygame.Clock().tick(60)
	ticking_tool += 1
	if ticking_tool % 5 == 0:
		animation_tick += 1