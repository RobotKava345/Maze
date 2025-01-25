#створи гру "Лабіринт"!
from pygame import *

FPS = 60
TILE_SIZE = 40
MAP_WIDTH, MAP_HEIGHT = 20, 15
WIDTH, HEIGHT = TILE_SIZE*MAP_WIDTH, TILE_SIZE*MAP_HEIGHT

#створи вікно гри
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Catch_up")
clock = time.Clock()


#задай фон сцени
bg = image.load("background.jpg")
bg = transform.scale(bg, (WIDTH, HEIGHT))
player_img = image.load("hero.png")
wall_img = image.load("wall.png")
#створи 2 спрайти та розмісти їх на сцені
class BaseSprite(sprite.Sprite):
    def __init__(self,image, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image, (width, height))
        self.rect = Rect(x,y, width, height)
    def draw(self, window):
        window.blit(self.image, self.rect)




class Player(BaseSprite):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)
        self.speed = 5
        self.hp = 100
        self.coins_counter = 0

    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -=self.speed
        if keys[K_d]:
           self.rect.x +=self.speed
        if keys[K_w]:
            self.rect.y -=self.speed
        if keys[K_s]:
            self.rect.y +=self.speed

player1 = Player(player_img,200,300, 100, 100)

walls = sprite.Group()


with open("map.txt", "r") as file:
    map = file.readlines()
    x, y = 0,0
    for row in map:
        for symbol in row:
            if symbol=='W':
               walls.add(BaseSprite(wall_img, x, y, TILE_SIZE, TILE_SIZE))
            x+=TILE_SIZE
        x = 0    
        y+= TILE_SIZE




run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    


    player1.update()


    window.blit(bg, (0,0))
    
    walls.draw(window)
    
    player1.draw(window)




    display.update()
    clock.tick(FPS)