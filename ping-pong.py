from pygame import *
from Player import Player
from Enemy import Enemy

window = display.set_mode((700, 500))
x, y = 600, 250
x1, y1 = 5, 250
x2, y2 = 350, 250
display.set_caption("Пинг-понг")
background = transform.scale(image.load("misterbeast.jpg"), (700, 500))

rocket = Player('ufo.png', x, y, 4, (100, 100), window)
skibidi = Player('ufo.png', x1, y1, 4, (100, 100), window)
ball = Enemy('asteroid.png', x2, y2, 4, (50, 50), window )
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!OH NO!', True, (100, 0, 0))

font2 = font.Font(None, 35)
lose2 = font1.render('PLAYER 2 LOSE! SKIBIDI !', True, (100, 0, 0))


FPS = 60
clock = time.Clock()

mixer.init()
mixer.music.load('musicmisterbeast.mp3')
mixer.music.play()


speed_x = 3
speed_y = 3

game = True
finish = False
while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False


    if sprite.collide_rect(rocket, ball) or sprite.collide_rect(skibidi, ball):
        speed_x *= -1




    if not finish:
        window.blit(background, (0, 0))
        rocket.update_l()
        skibidi.update_r()
        rocket.reset()
        skibidi.reset()
        ball.reset()

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 500 - 50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 653:
        finish = True
        window.blit(lose2, (200, 200))

    display.update()