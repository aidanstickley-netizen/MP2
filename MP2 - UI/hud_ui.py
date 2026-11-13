import pygame
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

frame_var = 0 #placeholder
heart_level = 0 #placeholder
Game_active = True

animation_tick = 0
ticking_tool = 0

def make_ui(x_cord, y_cord, mirror, bar, heart):
	bar_add_x = x_cord + 12
	mirror_buff = [0, 30, 60]

	if mirror:
		bar_add_x += 27
		mirror_buff = [60 + 60, 30 + 60, 0 + 60]

	heart_1 = 0
	heart_2 = 0
	heart_3 = 0
	if heart > 4:
		if heart > 8:
			heart_1 = 4
			heart_2 = 4
			heart_3 = heart - 8
		else:
			heart_1 = 4
			heart_2 = heart - 4
	else:
		heart_1 = heart

	Screen1.blit(mirror_image(ui_1, mirror), (x_cord, y_cord))
	Screen1.blit(mirror_image(Frames_bar[bar], mirror), (bar_add_x, y_cord + 54))

	Screen1.blit(mirror_image(Frames_heart[heart_1], mirror), (bar_add_x + mirror_buff[0], y_cord + 54 + 24))
	Screen1.blit(mirror_image(Frames_heart[heart_2], mirror), (bar_add_x + mirror_buff[1], y_cord + 54 + 24))
	Screen1.blit(mirror_image(Frames_heart[heart_3], mirror), (bar_add_x + mirror_buff[2], y_cord + 54 + 24))

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

	make_ui(15, 15, False, frame_var, heart_level)
	make_ui(585, 15, True, 5, 7)
	
	pygame.display.update()
	pygame.Clock().tick(60)
	ticking_tool += 1
	if ticking_tool % 5 == 0:
		animation_tick += 1