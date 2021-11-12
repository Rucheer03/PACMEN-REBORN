import pygame
import random

SCREEN_WIDTH = 608
SCREEN_HEIGHT = 672

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Ellipse(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ellipse
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Slime(pygame.sprite.Sprite):
    def __init__(self, x, y, change_x, change_y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the direction of the slime
        self.change_x = change_x
        self.change_y = change_y
        # Load image
        self.image = pygame.image.load("slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = "null"

    def update(self, horizontal_blocks, vertical_blocks, blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        for block in pygame.sprite.spritecollide(self,blocks[0],False):
            flag=False
            for i in range(1,16):
                for tmp in pygame.sprite.spritecollide(self,blocks[i],False):
                    tmp_block = tmp
                    block_index = i
                    flag = True
                    break
                if flag:
                    self.rect.centery = tmp_block.rect.centery
                    self.rect.centerx = tmp_block.rect.centerx
                    self.change_x = 0
                    self.change_y = 0
                    break

        for index in range(3,16):
            items = []
            for i, row in enumerate(enviroment()):
                for j, item in enumerate(row):
                    if item == index:
                        items.append((j * 32, i * 32))
            if self.rect.topleft in items:
                self.direction = self.get_direction(index)
                if self.direction == "left" and self.change_x == 0:
                    self.change_x = -2
                    self.change_y = 0
                elif self.direction == "right" and self.change_x == 0:
                    self.change_x = 2
                    self.change_y = 0
                elif self.direction == "up" and self.change_y == 0:
                    self.change_x = 0
                    self.change_y = -2
                elif self.direction == "down" and self.change_y == 0:
                    self.change_x = 0
                    self.change_y = 2


    def get_direction(self,index_of_item):
        if index_of_item == 3:
            l = ["right", "down"]
        elif index_of_item == 4:
            l=["left", "down"]
        elif index_of_item == 5:
            l=["left", "up"]
        elif index_of_item == 6:
            l=["right", "up"]
        elif index_of_item == 7:
            l=["left", "down", "right"]
        elif index_of_item == 8:
            l=["left", "up", "down"]
        elif index_of_item == 9:
            l=["right", "up", "left"]
        elif index_of_item == 10:
            l=["right", "up", "down"]
        elif index_of_item == 11:
            return "down"
        elif index_of_item == 12:
            return "left"
        elif index_of_item == 13:
            return "up"
        elif index_of_item == 14:
            return "right"
        elif index_of_item == 15:
            l=["left", "right", "up", "down"]
        try:
            l.remove(self.direction)
        finally:
            return random.choice(l)




def enviroment():
    with open('field.txt', 'r') as f:
        b = list(f.readlines())
    e = 0
    world = []
    for i in b:
        l = []
        for c in i:
            if c != '\n':
                if c == 'A':
                    l.append(10)
                elif c == 'B':
                    l.append(11)
                elif c == 'C':
                    l.append(12)
                elif c == 'D':
                    l.append(13)
                elif c == 'E':
                    l.append(14)
                elif c == 'F':
                    l.append(15)
                elif c == 'P': #player
                    l.append(16)
                elif c == 'G': #ghost
                    l.append(17)
                else:
                    l.append(int(c))
        world.append(tuple(l))
    grid = tuple(world)
    return grid


def draw_enviroment(screen):
    for i, row in enumerate(enviroment()):
        for j, item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3) #top
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3) #bottom
            elif item == 2:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3) #left
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3) #right
            elif item == 3:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3) #left
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3) #top
            elif item == 4:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3) #top
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3) #right
            elif item == 5:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3) #bottom
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3) #right
            elif item == 6:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3) #bottom
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3) #left
            elif item == 7:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3) #top
            elif item == 8:
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3) #right
            elif item == 9:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3) #bottom
            elif item == 10:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3) #left
            elif item == 11:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3) #top
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3) #right
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3) #left
            elif item == 12:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3) #bottom
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3) #top
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3) #right
            elif item == 13:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3) #bottom
                pygame.draw.line(screen, BLUE, [j * 32 + 32, i * 32], [j * 32 + 32, i * 32 + 32], 3) #right
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3) #left
            elif item == 14:
                pygame.draw.line(screen, BLUE, [j * 32, i * 32 + 32], [j * 32 + 32, i * 32 + 32], 3) #bottom
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32 + 32, i * 32], 3) #top
                pygame.draw.line(screen, BLUE, [j * 32, i * 32], [j * 32, i * 32 + 32], 3) #left