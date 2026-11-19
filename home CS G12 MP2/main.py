import pygame
import random
import math

class SpriteSheet():
    def __init__(self, image):
            self.sheet = image
    def get_image(self, frame, width, height, s):
        individual_img = pygame.Surface((width, height)).convert_alpha()
        individual_img.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        individual_img = pygame.transform.scale(individual_img, (width * s, height * s))
        return individual_img
class player(pygame.sprite.Sprite):
    def __init__(self, frames: list[pygame.Surface], name: str, spawning_location):
        super().__init__()
        self.frames = frames
        self.velocity = pygame.math.Vector2(0, 0)
        self.frame_index = 0
        self.animation=0.15
        self.image = self.frames[self.frame_index]
        self.name: str = name
        self.hp: int = 8
        self.max_hp: int = 8
        self.rings: int = 0
        self.money: int = 0
        self.rect = self.image.get_rect(center=spawning_location)
        self.inv: list[str]=[]
        self.status_effects: list[dict] = []
        self.equipped_weapon: str | None = "bare fists"
        self.on_ground = False
    def update(self, gravity, floor_y):
            self.velocity.y += gravity
            self.rect.move_ip(self.velocity)
            if self.rect.bottom >= floor_y:
                self.rect.bottom = floor_y
                self.velocity.y = 0
                self.on_ground = True
            else:
                self.on_ground = False
            self.animate()
    def animate(self):
        if not self.on_ground:
            self.frame_index = 1
            self.image = self.frames[1]
        else:
            self.frame_index = 0
            self.image = self.frames[0]
    def fire(self, cursor_location):
        direction = (pygame.math.Vector2(cursor_location[0], cursor_location[1]) - pygame.math.Vector2(self.rect.center[0], self.rect.center[1])).normalize()*10
        print(direction)
        Bullet_list.add(Bullets(self.rect.center, direction))
class WeponsOptriom:
    def __init__(self, name: str, damage: int, cost: int, currency_type: str, cooldown: int, hit_effect: int, crit_chance: float, aoe: bool):
        self.name= name
        self.damage= damage
        self.cost= cost
        self.currency_type= currency_type
        self.cooldown= cooldown
        self.hit_effect= hit_effect
        self.crit_chance= crit_chance
        self.aoe= aoe

effects = {
    1: {"name": "no effect", "damage_per_tick": 0, "duration": 0},
    2: {"name": "bleed", "damage_per_tick": 1, "duration": 2},
    3: {"name": "poison", "damage_per_tick": 1, "duration": 3},
    4: {"name": "burn", "damage_per_tick": 2, "duration": 2},
    5: {"name": "tetanus", "damage_per_tick": 1, "duration": 5},
    6: {"name": "stun", "damage_per_tick": 0, "duration": 1},
}
weapons_database = {
    "RPG": WeponsOptriom("RPG", 95, 80, "rings",20, 1, 0.05, True),
    "tommy gun": WeponsOptriom("tommy gun", 45, 35, "rings",1, 1, 0.10, True),
    "bat w nails": WeponsOptriom("bat w nails", 6, 2, "rings",1, 2, 0.10, False),
    "Plasma Cannon": WeponsOptriom("Plasma Cannon", 85, 75, "money",12, 4, 0.10, True),
    "Rocket Barrage": WeponsOptriom("Rocket Barrage", 55, 45, "rings",14, 1, 0.05, True),
    "Laser Pistol": WeponsOptriom("Laser Pistol", 22, 25, "money",4, 1, 0.15, False),
    "Nanite Spike": WeponsOptriom("Nanite Spike", 7, 3, "rings",3, 3, 0.25, False),
    "Smoke Slash": WeponsOptriom("Smoke Slash", 40, 22, "rings",9, 6, 0.15, True),
    "Katana Strike": WeponsOptriom("Katana Strike", 32, 18, "rings",4, 2, 0.20, False),
    "Shuriken Storm": WeponsOptriom("Shuriken Storm", 24, 14, "rings",2, 1, 0.05, True),
    "Kunai Throw": WeponsOptriom("Kunai Throw", 12, 8, "rings",1, 1, 0.10, False),
    "lighting": WeponsOptriom("lighting", 90, 60, "money",18, 6, 0.15, False),
    "fireball": WeponsOptriom("fireball", 50, 35, "money",14, 4, 0.10, True),
    "earth magic": WeponsOptriom("earth magic", 30, 22, "money",12, 1, 0.05, True),
    "wind magic": WeponsOptriom("wind magic", 16, 10, "money",6, 1, 0.10, False),
    "bone spear": WeponsOptriom("Bone Spear", 38, 30, "money",15, 2, 0.15, False),
    "shadow bolt": WeponsOptriom("Shadow Bolt", 25, 18, "money",9, 1, 0.10, False),
    "zombie bite": WeponsOptriom("Zombie Bite", 15, 10, "money",5, 3, 0.05, False),
    "scythe swing": WeponsOptriom("Scythe Swing", 5, 2, "money",3, 2, 0.15, True),
    "bare fists": WeponsOptriom("bare fists", 50, 0, "rings",1, 1, 0.05, False),
    "plunger": WeponsOptriom("plunger", 199, 150, "rings",15, 3, 0.05, False),
    "Broom": WeponsOptriom("Broom", 150, 200, "rings",12, 1, 0.05, False),
    "bic lighter": WeponsOptriom("bic lighter", 100, 300, "money",7, 4, 0.10, False),
    "Axe": WeponsOptriom("Axe", 200, 300, "rings",14, 2, 0.15, False),
    "curtainrod": WeponsOptriom("curtainrod", 200, 300, "rings",14, 1, 0.05, False),
    "watermelon": WeponsOptriom("watermelon", 400, 300, "rings",17, 1, 0.02, True),
    "Rusty nail": WeponsOptriom("Rusty nail", 100, 400, "rings",12, 5, 0.10, False),
    "towel": WeponsOptriom("towel", 200, 500, "rings",7, 1, 0.05, False),
    "Floor tile": WeponsOptriom("Floor tile", 550, 689, "rings",4, 2, 0.05, True),
}

pygame.init()
screen1 = pygame.display.set_mode((800,400))
gravity = 0.8
playerimage = pygame.image.load("dde.png").convert_alpha()
enermyimage = pygame.image.load("eed.png").convert_alpha()
p1_sheet_cut = SpriteSheet(playerimage)
p2_sheet_cut = SpriteSheet(enermyimage)
fw=150
fh=300
s=0.3
nf=2
p1_sheet=[p1_sheet_cut.get_image(i, fw, fh-25, s) for i in range(nf)]
p2_sheet = [p2_sheet_cut.get_image(i, fw, fh, s) for i in range(nf)]
floor_y = 350
class Bullets(pygame.sprite.Sprite):
    def __init__(self, spawning_location, Direction):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((227,174,27))
        self.rect = self.image.get_rect(center = spawning_location)
        self.direction = Direction
    def update(self):
        print(tuple([x for x in self.direction]))
        self.rect.move_ip(tuple([x for x in self.direction]))
        if(self.rect.top<0 or self.rect.left<0 or self.rect.right>800 or self.rect.bottom >400):
             self.kill()

player1 = player(p1_sheet,"hfud" ,(100, 200))
player2 = player(p2_sheet,"wer" ,(300, 200))

sprites_list1 = pygame.sprite.Group()
sprites_list1.add(player1)
sprites_list1.add(player2)

Bullet_list = pygame.sprite.Group()

gameactive = True
clock = pygame.time.Clock()

while gameactive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameactive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player1.on_ground:
                player1.velocity.y = -15
                player1.on_ground = False
            if event.key == pygame.K_a:
                player1.velocity.x -= 2
            if event.key == pygame.K_d:
                player1.velocity.x += 2
            if event.key == pygame.K_UP and player2.on_ground:
                player2.velocity. y = -15
                player2.on_ground = False
            if event.key == pygame.K_LEFT:
                player2.velocity.x -=2
            if event.key == pygame.K_RIGHT:
                player2.velocity.x += 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player1.velocity.x += 2
            if event.key == pygame.K_d:
                player1.velocity.x -= 2
            if event.key == pygame.K_LEFT:
                player2.velocity.x += 2
            if event.key == pygame.K_RIGHT:
                player2.velocity.x -= 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                  sprites_list1.sprites()[0].fire(event.pos)
            if event.button == 3:
                  player2.fire(event.pos)
    screen1.fill((0,0,0))
    pygame.draw.line(screen1, (200, 200, 200), (0, floor_y), (800, floor_y), 3)
    player1.update(gravity, floor_y)
    player2.update(gravity, floor_y)
    Bullet_list.update()
    sprites_list1.draw(screen1)
    Bullet_list.draw(screen1)
    
    pygame.display.update()
    clock.tick(60)