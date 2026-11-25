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

Game_active = True
animation_tick = 0
ticking_tool = 0
page = "title"
current_match = ""
buttons = []

while Game_active:
	if page == "title":
		buttons = [ui.button_maker(x_cord= 100, y_cord= 300, x_size= 180, y_size= 60, texture= 0, set_page_to= "battle1v1"),
	 		ui.button_maker(x_cord= 300, y_cord= 300, x_size= 180, y_size= 60, texture= 1, set_page_to= "battlevbot"),
	 		ui.button_maker(x_cord= 500, y_cord= 300, x_size= 180, y_size= 60, texture= 2, set_page_to= "settings")]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for x in range(len(buttons)):
					if (buttons[x].x_cord < event.pos[0] < buttons[x].x_cord_max) and (buttons[x].y_cord < event.pos[1] < buttons[x].y_cord_max):
						page = buttons[x].page_output
					if (event.pos[0] < 10) and (event.pos[1] < 10):
						print("egg")
				#ui.new_event_popup(0, 0, active= True) fix

		Screen1.fill(color)
		for x in range(len(buttons)):
			ui.flet_button(buttons[x].x_cord, buttons[x].y_cord, buttons[x].x_size, buttons[x].y_size, buttons[x].texture_no)

	if page == "battle1v1":
		current_match = "1v1"
		buttons = [ui.button_maker(x_cord= 740, y_cord= 340, texture= 2, set_page_to= "pause")]
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
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and mov.player1.alive():
					mov.player1.fire(event.pos)
				if event.button == 3 and mov.player2.alive():
					mov.player2.fire(event.pos)
				if event.button == 1:
					for x in range(len(buttons)):
						if (buttons[x].x_cord < event.pos[0] < buttons[x].x_cord_max) and (buttons[x].y_cord < event.pos[1] < buttons[x].y_cord_max):
							page = buttons[x].page_output


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

		for x in range(len(buttons)):
			ui.flet_button(buttons[x].x_cord, buttons[x].y_cord, buttons[x].x_size, buttons[x].y_size, buttons[x].texture_no)

	if page == "battlevbot":
		current_match = "vbot"
		buttons = [ui.button_maker(x_cord= 740, y_cord= 340, texture= 2, set_page_to= "pause")]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					for x in range(len(buttons)):
						if (buttons[x].x_cord < event.pos[0] < buttons[x].x_cord_max) and (buttons[x].y_cord < event.pos[1] < buttons[x].y_cord_max):
							page = buttons[x].page_output


		Screen1.fill(color3)

		ui.make_event_display(42)

		ui.display_num(ticking_tool, 500, 300, 1)

		ui.make_hud(15, 15, False, 1, 2, 3, 4)

		for x in range(len(buttons)):
			ui.flet_button(buttons[x].x_cord, buttons[x].y_cord, buttons[x].x_size, buttons[x].y_size, buttons[x].texture_no)

	if page == "settings":
		buttons = [ui.button_maker(x_cord= 100, y_cord= 200, x_size= 100, y_size= 100, texture= 0, set_page_to= "title")]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for x in range(len(buttons)):
					if (buttons[x].x_cord < event.pos[0] < buttons[x].x_cord_max) and (buttons[x].y_cord < event.pos[1] < buttons[x].y_cord_max):
						page = buttons[x].page_output
						
		Screen1.fill(color3)

		for x in range(len(buttons)):
			ui.flet_button(buttons[x].x_cord, buttons[x].y_cord, buttons[x].x_size, buttons[x].y_size, buttons[x].texture_no)

	if page == "pause":
		buttons = [ui.button_maker(x_cord= 100, y_cord= 200, x_size= 100, y_size= 100, texture= 0, set_page_to= "battle"+ current_match),
		           ui.button_maker(x_cord= 200, y_cord= 200, x_size= 100, y_size= 100, texture= 1, set_page_to= "title")]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for x in range(len(buttons)):
					if (buttons[x].x_cord < event.pos[0] < buttons[x].x_cord_max) and (buttons[x].y_cord < event.pos[1] < buttons[x].y_cord_max):
						page = buttons[x].page_output
						

		for x in range(len(buttons)):
			ui.flet_button(buttons[x].x_cord, buttons[x].y_cord, buttons[x].x_size, buttons[x].y_size, buttons[x].texture_no)
	
	pygame.display.update()
	pygame.Clock().tick(60)
	ticking_tool += 1
	if ticking_tool % 5 == 0:
		animation_tick += 1
	#ui.tick_event_popup() fix