import pygame

pygame.init()   #this will initiate pygame for your program
Screen1 = pygame.display.set_mode((800,400))    
color = (100, 100, 255)
Screen1.fill(color)

scr = pygame.image.load("graphics/scr_rotate.png")
bar = pygame.image.load("graphics/hit_bar.png")
hearts = pygame.image.load("graphics/hearts.png")
ui_1 = pygame.image.load("graphics/equipped_item_ui.png")
ui_1 = pygame.transform.scale(ui_1, (66 * 3, 17 * 3))

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

i = 0
frame_var = 0
heart_level = 0
Game_active = True

def make_ui(x, y, mirror, bar, heart):
	Screen1.blit(ui_1, (x,y))
	Screen1.blit(Frames_bar[bar], (x + 12, y + 53))
	Screen1.blit(Frames_heart[heart], (100,200))

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
						if heart_level < 4:
							heart_level +=1
						else:
							heart_level = 0

	Screen1.fill(color)

	Screen1.blit(Frames[i], (200,200))
	
	if i < 7:
		i+=1
	else:
		i = 0

	make_ui(100, 100, False, frame_var, heart_level)
	make_ui(400, 100, False, 5, 5)
	
	pygame.display.update()
	pygame.Clock().tick(10)