from pyautogui import confirm
import Tamagotchi
import pygame
import minigames.feed

# CONSTANTS

WIDTH = 480
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BEIGE = (207, 185, 151)

DEAD = "gfx\\dead.png"           


# INIT
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tamagachi")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# DRAW FUNCTIONS

def stats(name, bored, hunger, shit): # Display Tamagachi's stats above
    font = pygame.font.SysFont(None, 24)
    printname = font.render("Name: " + name, True, BLUE)
    screen.blit(printname, (20, 20))
    hp = font.render("Bored: " + str(bored), True, BLUE)
    screen.blit(hp, (20, 40))
    hunger = font.render("Hunger: " + str(hunger), True, BLUE)
    screen.blit(hunger, (20, 60))
    shit = font.render("Shit: " + str(shit), True, BLUE)
    screen.blit(shit, (20, 80))

def faces(state, x, y):
    pos = (x,y)
    screen.blit(pygame.image.load(state), pos)


name = input("Name the child: ")
egg = Tamagotchi.Tamagotchi()

running = True
while running:

    
    clock.tick(FPS)     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # start


    if not egg.dead:
        
        dead = egg.die()
        mood = egg.determine_mood()
       
        stats(name, egg.bored, egg.hunger, egg.poo_count)
        faces(mood, 160, 160)

        egg.worsen()
        egg.move()

    # end

    if egg.dead:
        stats(name + "has died", 10, 10, 10)
        faces(DEAD, 160, 160)

    pygame.display.flip()       

pygame.quit()