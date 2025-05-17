from pygame import *

background = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((700, 500))
window.fill(background)

playerL = transform.scale(image.load('playerL.jpeg'), (35, 200))
playerR = transform.scale(image.load('playerR.jpeg'), (35, 200))
ball = transform.scale(image.load('ball.png'), (65, 65))

font.init()
font = font.SysFont('Arial', 70)

clock = time.Clock()
FPS = 60
game = True
finish = False

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (35, 200))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500 - 205:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500 - 205:
            self.rect.y += self.speed

playerL = Player('playerL.jpeg', 20, 150, 3)
playerR = Player('playerR.jpeg', 650, 150, 3)

while game:
    if finish != True:
        window.fill(background)
        playerL.updateL()
        playerR.updateR()
        playerL.reset()
        playerR.reset()


            
            #finish = True
    
    clock.tick(FPS)
    display.update()

    for e in event.get():
        if e.type == QUIT:
            game = False