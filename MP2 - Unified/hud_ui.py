import pygame
import random
# frame rate is 60/s
# animation frame rate is 12/s
# clean up the code for making character spritesheets

pygame.init()
Screen1 = pygame.display.set_mode((800,400))    
color = (100, 100, 255)
Screen1.fill(color)

scr_sprite_sheet = pygame.image.load("graphics/scr_rotate.png").convert_alpha()
bar_sprite_sheet = pygame.image.load("graphics/hud/hit_bar.png").convert_alpha()
hearts_sprite_sheet = pygame.image.load("graphics/hud/hearts.png").convert_alpha()

ui_1 = pygame.image.load("graphics/hud/equipped_item_ui.png").convert_alpha()
ui_1 = pygame.transform.scale(ui_1, (66 * 3, 17 * 3))

ui_2 = pygame.image.load("graphics/hud/currency_marker_ui.png").convert_alpha()
ui_2 = pygame.transform.scale(ui_2, (9 * 3, 16 * 3))

ui_3 = pygame.image.load("graphics/hud/current_event_ui.png")
ui_3 = pygame.transform.scale(ui_3, (44 * 3, 30 * 3))

numbers_black = pygame.image.load("graphics/hud/zero_to_nine_num_black.png").convert_alpha()
numbers_white = pygame.image.load("graphics/hud/zero_to_nine_num_white.png").convert_alpha()

character = pygame.image.load("graphics/characters/scr_guy_blue.png").convert_alpha()
def get_player_spritesheet():
	print("hello")

equipment = pygame.image.load("graphics/equipment/weapons_icon.png").convert_alpha()

four_buttons = pygame.image.load("graphics/user_interface/four_buttons.png").convert_alpha()

def gather_frames(to_be_cut, x_size, y_size, mult, frame_count, row_count = 0, mirroring = False):
	Animation_object = spriteSheet(mirror_image(to_be_cut, mirroring))
	return [Animation_object.get_frame(i, x_size, y_size, mult, row= row_count) for i in range(frame_count)]

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
	def get_frame(self, frame, width, height, scale, row = 0):
		individual_img = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
		individual_img.blit(self.sheet, (0, 0), ((frame * width), (row * height), width, height))
		individual_img = pygame.transform.scale(individual_img, (width * scale, height * scale)).convert_alpha()
		return individual_img

class button_maker():
	def __init__(self, x_cord: int, y_cord: int, x_size: int = 60, y_size: int = 60, texture: int = 0, set_page_to: str = ""):
		self.x_cord = x_cord
		self.y_cord = y_cord
		self.x_cord_max = x_cord + x_size
		self.y_cord_max = y_cord + y_size
		self.x_size = x_size
		self.y_size = y_size
		self.page_output = set_page_to
		self.texture_no = texture

class event_popup_maker():
	def __init__(self, x_cord, y_cord, texture, lifetime):
		self.lifeti = x_cord
		self.y_cord = y_cord
		self.texture = texture
		self.lifetime = lifetime
scr_single = gather_frames(scr_sprite_sheet, 9, 9, 3, 8)
damage_bar = gather_frames(bar_sprite_sheet, 49, 7, 3, 8)
Frames_heart = gather_frames(hearts_sprite_sheet, 9, 9, 3, 5)

indiviual_button = gather_frames(four_buttons, 20, 20, 3, 4)

number = [gather_frames(numbers_black, 3, 7, 3, 10), 
          gather_frames(numbers_white, 3, 7, 3, 10)]
	
held_equipment = gather_frames(equipment, 13, 13, 3, 75)
held_equipment = gather_frames(pygame.image.load("graphics/equipment/weapons_scrw_v2.png"), 13, 13, 3, 10) # temp

player = {
	"walk": gather_frames(character, 13, 21, 4, 5),
	"idle": gather_frames(character, 13, 21, 4, 5, 1),
	"attack": gather_frames(character, 13, 21, 4, 5, 3),
	"jump": gather_frames(character, 13, 21, 4, 5, 4),
	"damage": gather_frames(character, 13, 21, 4, 5, 5)
	}

def get_player_texture(player_spritesheet):
	return {
	"walk": gather_frames(player_spritesheet, 13, 21, 3, 5),
	"idle": gather_frames(player_spritesheet, 13, 21, 3, 5, 1),
	"attack": gather_frames(player_spritesheet, 13, 21, 3, 5, 3),
	"jump": gather_frames(player_spritesheet, 13, 21, 3, 5, 4),
	"damage": gather_frames(player_spritesheet, 13, 21, 3, 5, 5)
	}
def get_player_texture2(player_spritesheet_id: str):
	player_spritesheet = pygame.image.load("graphics/equipment/scr_guy"+ player_spritesheet_id +".png")
	return {
	"walk": gather_frames(player_spritesheet, 13, 21, 3, 5),
	"idle": gather_frames(player_spritesheet, 13, 21, 3, 5, 1),
	"attack": gather_frames(player_spritesheet, 13, 21, 3, 5, 3),
	"jump": gather_frames(player_spritesheet, 13, 21, 3, 5, 4),
	"damage": gather_frames(player_spritesheet, 13, 21, 3, 5, 5)
	}

frame_var = 0 #placeholder
heart_level = 0 #placeholder
Game_active = False # set to true to ativate this code

animation_tick = 0
ticking_tool = 0
event_popup_storage = [0, 0, 0, 0, False]

def flet_button(xcord, ycord, xsize, ysize, value: int = 0):
	button_blit_tool = indiviual_button[value]
	button_blit_tool = pygame.transform.scale(button_blit_tool, (xsize, ysize))
	Screen1.blit(button_blit_tool, (xcord, ycord))

def display_num(value, xpos = 0, ypos = 0, colour_number = 0):
	value2 = str(value)
	for x in range(len(value2)):
		Screen1.blit(number[colour_number][int(value2[x])], (xpos + 12 * x, ypos))

def display_wallet(xcord, ycord, scr_count = 0, money_count = 0, money_display_move = 0):
	
	Screen1.blit(ui_2, (money_display_move, ycord))
	display_num(scr_count, xcord, ycord)
	display_num(money_count, xcord, ycord + 27)

def make_hud(x_cord, y_cord, mirror, bar, heart, scr_value = 100, money_value = 30, equip_slot_1 = 0, equip_slot_2 = 1, equip_slot_3 = 2):
	bar_add_x = x_cord + 12
	number_x_offset = x_cord + 42
	mirror_buff = [0, 30, 60]
	held_equipment_mirror = [6, 66, 126]
	money_display = bar_add_x

	if mirror:
		bar_add_x += 27
		mirror_buff = [120, 90, 60]
		held_equipment_mirror = [153, 93, 33]
		number_x_offset += 81
		money_display += 147

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
	Screen1.blit(mirror_image(damage_bar[bar], mirror), (bar_add_x, y_cord + 54))

	display_wallet(number_x_offset, y_cord + 114, scr_value, money_value, money_display_move = money_display)

	for x in range(3):
		Screen1.blit(mirror_image(Frames_heart[hearts[x]], mirror), (bar_add_x + mirror_buff[x], y_cord + 78))

	Screen1.blit(mirror_image(held_equipment[equip_slot_1], mirror), (x_cord + held_equipment_mirror[0], y_cord + 6))
	Screen1.blit(mirror_image(held_equipment[equip_slot_2], mirror), (x_cord + held_equipment_mirror[1], y_cord + 6))
	Screen1.blit(mirror_image(held_equipment[equip_slot_3], mirror), (x_cord + held_equipment_mirror[2], y_cord + 6))

def make_event_display(time, xpos = 333, ypos = 9):
	Screen1.blit(ui_3, (xpos, ypos))
	display_num(time, xpos + 45 + 12 - 2, ypos + 66)

def new_event_popup(x_cord: int, y_cord: int, texture: int = 0, lifetime: int = 100, active = True):
	global event_popup_storage
	event_popup_storage = [x_cord, y_cord, texture, lifetime, active]

def tick_event_popup():
	global event_popup_storage
	print(len(event_popup_storage))
	event_popup_storage[0] += 1
	event_popup_storage[3] -= 1
	print(event_popup_storage[3])
	if event_popup_storage[3] <= 0:
		event_popup_storage = []
		print(len(event_popup_storage))
		print("size reduced")
	if event_popup_storage[4]:
		Screen1.blit(indiviual_button[event_popup_storage[2]], (event_popup_storage[0], event_popup_storage[1]))

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

	Screen1.blit(scr_single[animation_tick % 8], (200,200))

	make_event_display(42)

	display_num(ticking_tool, 500, 300, 1)

	make_hud(15, 15, False, frame_var, heart_level, frame_var, heart_level)
	make_hud(585, 15, True, 5, 7)
	
	pygame.display.update()
	pygame.Clock().tick(60)
	ticking_tool += 1
	if ticking_tool % 5 == 0:
		animation_tick += 1