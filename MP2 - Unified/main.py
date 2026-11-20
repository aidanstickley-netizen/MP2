import pygame
import random
import hud_ui as ui
import test as mov
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
page = "battle1v1"

	
while Game_active:
	if page == "title":
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				page = "battle1v1"
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1 & (100 < event.pos[0] < 200) & (200 < event.pos[1] < 400):
				page = "battle1vbot"

		Screen1.fill(color)

		ui.flet_button(100, 200, 100, 200)

	if page == "battle1v1":
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w and mov.player1.on_ground:
					mov.player1.velocity.y = -15
					mov.player1.on_ground = False
				if event.key == pygame.K_a:
					mov.player1.velocity.x -= 2
				if event.key == pygame.K_d:
					mov.player1.velocity.x += 2
				if event.key == pygame.K_UP and mov.player2.on_ground:
					mov.player2.velocity. y = -15
					mov.player2.on_ground = False
				if event.key == pygame.K_LEFT:
					mov.player2.velocity.x -=2
				if event.key == pygame.K_RIGHT:
					mov.player2.velocity.x += 2
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					mov.player1.velocity.x += 2
				if event.key == pygame.K_d:
					mov.player1.velocity.x -= 2
				if event.key == pygame.K_LEFT:
					mov.player2.velocity.x += 2
				if event.key == pygame.K_RIGHT:
					mov.player2.velocity.x -= 2
				if event.key == pygame.K_c:
					page = "battle1vbot"
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and mov.player1.alive():
					mov.player1.fire(event.pos)
				if event.button == 3 and mov.player2.alive():
					mov.player2.fire(event.pos)


		Screen1.fill((100,0,0))
		pygame.draw.line(Screen1, (200, 200, 200), (0, mov.floor_y), (800, mov.floor_y), 3)
		mov.player1.update(mov.gravity, mov.floor_y)
		mov.player2.update(mov.gravity, mov.floor_y)
		mov.update_bullets()
		mov.sprites_list1.draw(Screen1)
		mov.Bullet_list.draw(Screen1)

		ui.make_event_display(42)

		ui.make_hud(15, 15, False, mov.player1.hp -1, mov.player1.hearts, mov.player1.rings, mov.player1.money)
		ui.make_hud(585, 15, True, mov.player2.hp -1, mov.player2.hearts, mov.player2.rings, mov.player2.money)

	if page == "battle1vbot":
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