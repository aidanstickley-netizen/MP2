import pygame
import random
import hud_ui as ui
# frame rate is 60/s
# animation frame rate is 12/s
particle = 0

active_buttons = [[100, 200, 100, 200]]

pygame.init()
Screen1 = pygame.display.set_mode((800,400))
color = (100, 100, 255)
Screen1.fill(color)
color2 = (100, 200, 255)
color3 = (200, 200, 255)

frame_var = 0 #placeholder
heart_level = 0 #placeholder
Game_active = True
animation_tick = 0
ticking_tool = 0
global page
page = "title"

	
while Game_active:
	if page == "title":
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				page = "battle1vbot"
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1 & (100 < event.pos[0] < 200) & (200 < event.pos[1] < 400):
				page = "battle1vbot"

		Screen1.fill(color)

		ui.flet_button(100, 200, 100, 200)

	elif page == "battle1v1":
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
				elif event.key == pygame.K_c:
					page = "battle1vbot"

		Screen1.fill(color2)

		ui.make_event_display(42)

		ui.display_num(ticking_tool, 500, 300, 1)

		ui.make_hud(15, 15, False, frame_var, heart_level, frame_var, heart_level)
		ui.make_hud(585, 15, True, 5, 7)

	elif page == "battle1vbot":
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
				elif event.key == pygame.K_c:
					page = "title"

		Screen1.fill(color3)

		ui.make_event_display(42)

		ui.display_num(ticking_tool, 500, 300, 1)

		ui.make_hud(15, 15, False, frame_var, heart_level, frame_var, heart_level)
	
	pygame.display.update()
	pygame.Clock().tick(60)
	ticking_tool += 1
	if ticking_tool % 5 == 0:
		animation_tick += 1