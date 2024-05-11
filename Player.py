from GameSprite import GameSprite
from pygame import *
class Player(GameSprite):
    # метод управления стрелками
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
        if keys_pressed[K_s]:
            self.rect.y += self.speed


    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed



