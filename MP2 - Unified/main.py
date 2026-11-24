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
buttons = []

while Game_active:
	buttons = [[100, 300, 180, 60, "battle1v1", 0], [300, 300, 180, 60, "battlevbot", 1], [500, 300, 180, 60, "settings", 2]]
	if page == "title":
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				page = "battle1v1"
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for x in range(len(buttons)):
					if (buttons[x][0] < event.pos[0] < buttons[x][0] + buttons[x][2]) and (buttons[x][1] < event.pos[1] < buttons[x][1] + buttons[x][3]):
						page = buttons[x][4]
					if (event.pos[0] < 10) and (event.pos[1] < 10):
						print("egg")

		Screen1.fill(color)
		for x in range(len(buttons)):
			ui.flet_button(buttons[x][0], buttons[x][1], buttons[x][2], buttons[x][3], buttons[x][5])

	if page == "battle1v1":
		buttons = [[740, 340, 60, 60, "title", 2]]
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
					page = "battlevbot"
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and mov.player1.alive():
					mov.player1.fire(event.pos)
				if event.button == 3 and mov.player2.alive():
					mov.player2.fire(event.pos)
				if event.button == 1:
					for x in range(len(buttons)):
						if (buttons[x][0] < event.pos[0] < buttons[x][0] + buttons[x][2]) and (buttons[x][1] < event.pos[1] < buttons[x][1] + buttons[x][3]):
							page = buttons[x][4]


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
			ui.flet_button(buttons[x][0], buttons[x][1], buttons[x][2], buttons[x][3], buttons[x][5])

	if page == "battlevbot":
		buttons = [[740, 340, 60, 60, "title", 2]]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					page = "title"
				elif event.key == pygame.K_v:
					page = "battle1v1"
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					for x in range(len(buttons)):
						if (buttons[x][0] < event.pos[0] < buttons[x][0] + buttons[x][2]) and (buttons[x][1] < event.pos[1] < buttons[x][1] + buttons[x][3]):
							page = buttons[x][4]


		Screen1.fill(color3)

		ui.make_event_display(42)

		ui.display_num(ticking_tool, 500, 300, 1)

		ui.make_hud(15, 15, False, 1, 2, 3, 4)

		for x in range(len(buttons)):
			ui.flet_button(buttons[x][0], buttons[x][1], buttons[x][2], buttons[x][3], buttons[x][5])

	if page == "settings":
		buttons = [[100, 200, 100, 200, "title", 0]]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Game_active = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for x in range(len(buttons)):
					if (buttons[x][0] < event.pos[0] < buttons[x][0] + buttons[x][2]) and (buttons[x][1] < event.pos[1] < buttons[x][1] + buttons[x][3]):
						page = buttons[x][4]

		Screen1.fill(color)
		for x in range(len(buttons)):
			ui.flet_button(buttons[x][0], buttons[x][1], buttons[x][2], buttons[x][3], buttons[x][5])
	
	pygame.display.update()
	pygame.Clock().tick(60)
	ticking_tool += 1
	if ticking_tool % 5 == 0:
		animation_tick += 1