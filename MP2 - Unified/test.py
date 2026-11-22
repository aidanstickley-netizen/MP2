import pygame
import random
import math
import hud_ui as ui

class SpriteSheet():
    def __init__(self, image):
            self.sheet = image
    def get_image(self, frame, width, height, s):
        individual_img = pygame.Surface((width, height)).convert_alpha()
        individual_img.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        individual_img = pygame.transform.scale(individual_img, (width * s, height * s))
        return individual_img

class player(pygame.sprite.Sprite):
    def __init__(self, frames: dict[str, pygame.Surface], name: str, spawning_location):
        super().__init__()
        self.frames = frames
        self.frame_index: float = 0.0
        self.velocity = pygame.math.Vector2(0, 0)
        self.state = "idle"
        self.mirror= False
        self.animation=0.15
        self.image = self.frames[self.state][0]
        self.name: str = name
        self.hp: int = 8
        self.max_hp: int = 8
        self.hearts: int = 12
        self.max_hearts: int = 12
        self.rings: int = 0
        self.money: int = 0
        self.rect = self.image.get_rect(center= spawning_location)
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
    def take_damage(self, amount: int):
        self.hp -= amount
        while self.hp <= 0 and self.hearts > 0:
            self.hearts -= 1
            if self.hearts > 0:
                self.hp += self.max_hp
            else:
                self.hp = 0
    def animate(self):
        if self.velocity.x < 0:
            self.mirror = True
        elif self.velocity.x > 0:
            self.mirror = False
        if not self.on_ground:
            self.state = "jump"
        elif self.velocity.x != 0:
            self.state = "walk"
        else:
            self.state = "idle"
        current_frames = self.frames[self.state]
        self.frame_index = (self.frame_index + self.animation) % len(current_frames)
        base_image = current_frames[int(self.frame_index)]
        if self.mirror:
            self.image = pygame.transform.flip(base_image, True, False)
        else:
            self.image = base_image
        if self.frame_index >= len(current_frames):
            self.frame_index = 0.0

        base_image = current_frames[int(self.frame_index)]
        if self.mirror:
            self.image = pygame.transform.flip(base_image, True, False)
        else:
            self.image = base_image
    def fire(self, cursor_location):
        aim_vector = pygame.math.Vector2(cursor_location) - pygame.math.Vector2(self.rect.center)
        if aim_vector.length() > 0:
            direction = aim_vector.normalize() * 10
            Bullet_list.add(Bullets(self.rect.center, direction, owner=self))
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
class DefenceOption:
    def __init__(self,name,block_amount,cost,currency,cooldown,duration,dodge_chance,is_aoe_shield):
        self.name = name
        self.block_amount = block_amount
        self.cost = cost
        self.currency = currency
        self.cooldown = cooldown
        self.duration = duration
        self.dodge_chance = dodge_chance 
        self.is_aoe_shield = is_aoe_shield 
    def mitigate_damage(self, incoming_damage, is_aoe_attack=False):
        effective_block = self.block_amount
        if is_aoe_attack and not self.is_aoe_shield:
            effective_block *= 0.5

        final_damage = max(0, incoming_damage - effective_block)
        return final_damage
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
    "arcane missile": WeponsOptriom("Arcane Missile", 18, 12, "money", 2, 1, 0.20, False),
    "venom cloud": WeponsOptriom("Venom Cloud", 15, 25, "money", 11, 3, 0.05, True),
    "meteor shower": WeponsOptriom("Meteor Shower", 140, 110, "money", 25, 4, 0.10, True),
    "blood siphon": WeponsOptriom("Blood Siphon", 35, 40, "money", 10, 2, 0.10, False),
    "chain lightning": WeponsOptriom("Chain Lightning", 65, 55, "money", 14, 6, 0.15, True),
    "water jet": WeponsOptriom("Water Jet", 20, 15, "money", 4, 1, 0.10, False),
    "solar flare": WeponsOptriom("Solar Flare", 80, 70, "money", 16, 4, 0.15, True),
    "necrotic touch": WeponsOptriom("Necrotic Touch", 42, 32, "money", 8, 5, 0.10, False),
    "eldritch blast": WeponsOptriom("Eldritch Blast", 55, 45, "money", 7, 1, 0.20, False),
    "frost nova": WeponsOptriom("Frost Nova", 45, 38, "money", 13, 6, 0.05, True),
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
player1_image = pygame.image.load("graphics/characters/scr_guy_blue.png").convert_alpha()
player2_image = pygame.image.load("graphics/characters/scr_guy_purple.png").convert_alpha()
fw=160
fh=300
s=0.3
nf=2
p1_sheet = ui.get_player_texture(player1_image)
p2_sheet = ui.get_player_texture(player2_image)
floor_y = 350

class Bullets(pygame.sprite.Sprite):
    def __init__(self, spawning_location, direction, owner, damage=3):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((227, 174, 27))
        self.rect = self.image.get_rect(center=spawning_location)
        self.direction = direction
        self.owner = owner
        self.damage = damage
    def update(self):
        self.rect.move_ip(self.direction)
        if self.rect.top < 0 or self.rect.left < 0 or self.rect.right > 800 or self.rect.bottom > 400:
            self.kill()
def update_bullets():
    Bullet_list.update()
    for bullet in Bullet_list:
        hit_players = pygame.sprite.spritecollide(bullet, sprites_list1, False)
        for target in hit_players:
            if target != bullet.owner:
                target.take_damage(bullet.damage)
                bullet.kill()
                if target.hearts <= 0:
                    target.kill()
                break
player1 = player(p1_sheet,"hfud" ,(100, 200))
player2 = player(p2_sheet,"wer" ,  (300, 200))

sprites_list1 = pygame.sprite.Group()
sprites_list1.add(player1)
sprites_list1.add(player2)

Bullet_list = pygame.sprite.Group()

gameactive = False
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
                player1.fire(event.pos)
            if event.button == 3:
                player2.fire(event.pos)
    screen1.fill((0,0,0))
    pygame.draw.line(screen1, (200, 200, 200), (0, floor_y), (800, floor_y), 3)
    player1.update(gravity, floor_y)
    player2.update(gravity, floor_y)
    Bullet_list.update()
    for bullet in Bullet_list:
        hit_players = pygame.sprite.spritecollide(bullet, sprites_list1, False)
        for target in hit_players:
            if target != bullet.owner:
                target.hp -= bullet.damage
                bullet.kill()
                if target.hp <= 0:
                    target.kill()
                break
    sprites_list1.draw(screen1)
    Bullet_list.draw(screen1)
    
    pygame.display.update()
    clock.tick(60)
