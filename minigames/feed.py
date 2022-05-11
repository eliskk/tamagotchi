'''
Game where you choose click items in a sequence

the success rate how much hunger fixes

EXAMPLE:

80% correct click rate over 1 time => if hunger = 1 then hunger becomes 20% 
(4/5)

'''

import pygame
import random

# Constants

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (165,42,42)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Feed the child")
clock = pygame.time.Clock() 

# Variables

timeleft = 15
order = []

# Functions

def generate_order(): # test run this
  
  order_num = []
  order_food = []
  
  for i in range(4):
    order_num.append(random.randint(4))
  
  for food in order_num:
    
    match food:
      case 0:
        order_food.append("fries")
      case 1:
        order_food.append("apple")
      case 2:
        order_food.append("rice")
      case 3:
        order_food.append("chicken")
      case 4:
        order_food.append("pizza")
  
  return order_food
  
all_sprites = pygame.sprite.group()

running = True
while running:

    clock.tick(FPS)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    
    all_sprites.update()


   
    screen.fill(WHITE)

    

    all_sprites.draw(screen)
    
    
    
    pygame.display.flip()       

pygame.quit()
