import pygame
import random
BLUE_BLOBS = 10
GREEN_BLOBS = 5
RED_BLOBS = 3

WIDTH = 800
HEIGHT = 500
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (255,0,0)
RED = (0,255,0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class Blob:

    def __init__(self,color):
        self.x = random.randrange(0,WIDTH)
        self.y = random.randrange(0,HEIGHT)
        self.size = random.randrange(5,10)
        self.color = color
    def move(self):
        self.move_x = random.randrange(-2,2)
        self.move_y = random.randrange(-2,2)
        self.x += self.move_x
        self.y += self.move_y
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT


def background(blob_list):
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display,blob.color,[blob.x,blob.y],blob.size)
            blob.move()
    pygame.display.update()

def main():
    blue_blobs = dict(enumerate([Blob(BLUE) for i in range(BLUE_BLOBS)]))
    green_blobs = dict(enumerate([Blob(GREEN) for i in range(GREEN_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED) for i in range(RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background([blue_blobs,green_blobs,red_blobs])
        clock.tick(20)
if __name__ == '__main__':
    main()

















