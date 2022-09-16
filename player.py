import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):

        super().__init__(groups)
        self.image = pygame.image.load("graphics/tiles/char/down/0.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)#,height=TILESIZE*2
        self.hitbox = self.rect.inflate(0, -2)#-6

        #graphics setup
        self.import_player_assets()
        self.status = "down_idle"
        self.frame_index = 0
        self.animation_speed = 0.15

        #movement
        self.direction = pygame.math.Vector2()
        self.speed = 2 #5

        self.cooldown = 400#brauchen wir erstmal nicht (können später damit dinge die einen cooldown haben implementieren)
        self.cooldowntime = None
        self.attacking = False

        self.obstacle_sprites = obstacle_sprites
    def import_player_assets(self):
        character_path = "graphics/tiles/char/"
        self.animations = {
            "up": [], "down": [], "left": [], "right": [],
            "up_idle": [], "down_idle": [], "left_idle": [], "right_idle": [],
        }
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder_tutorial(full_path)
    def input(self): #mal sehen ob methoden oder doch noch extra klasse für input
        keys = pygame.key.get_pressed()
        #movement
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        else:
            self.direction.x = 0
        #attacking (brauchen wir so nicht aber einfach damit wir ähnliche sachen machen können)
        if keys[pygame.K_LCTRL] and not self.attacking:
            self.attacking = True
            self.cooldowntime = pygame.time.get_ticks()

    def get_status(self):
        #idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not "idle" in self.status:
                self.status = self.status + "_idle"

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x >0: #rechts
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #links
                        self.hitbox.left = sprite.hitbox.right
        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #up
                        self.hitbox.top = sprite.hitbox.bottom
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.cooldowntime >= self.cooldown:
                self.attacking = False
    def animate(self):
        animation = self.animations[self.status]

        #loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        #set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
