import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player setup
player = pygame.Rect(375, 100, 50, 50)
vel_y = 0
gravity = 0.8
jump_strength = -15
on_ground = False

# Floor setup
floor_y = 500

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        # Jump only when on the ground
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                vel_y = jump_strength
                on_ground = False

    # 1. Apply gravity to vertical velocity
    vel_y += gravity
    
    # 2. Apply velocity to player's y-position
    player.y += vel_y

    # 3. Check floor collision
    if player.bottom >= floor_y:
        player.bottom = floor_y
        vel_y = 0
        on_ground = True

    # Drawing
    screen.fill((30, 30, 30))
    pygame.draw.line(screen, (200, 200, 200), (0, floor_y), (WIDTH, floor_y), 3)
    pygame.draw.rect(screen, (0, 200, 100), player)

    pygame.display.flip()
    clock.tick(60)
