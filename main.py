import random
from pyautogui import confirm
import pygame

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

HAPPY = "tamagotchi/gfx/happy.jpg"
MID = "tamagotchi/gfx/mid.jpg"
SAD = "tamagotchi/gfx/sad.png"
DEAD = "tamagotchi/gfx/dead.png"
POO = "tamagotchi/gfx/poo.png"

# VARIABLES

class Tamagotchi:

    def __init__(self):
        self.hunger = 0
        self.bored = 0
        self.poo_count = 0
        self.mood = MID
        self.dead = False

        self.last_action = 3 # 0 = hunger, 1 = bored, 2 = poo
    
    def hungry(self):
        self.hunger += 1

    def get_bored(self):
        self.bored += 1

    def poo(self):
        self.poo_count += 1

    def die(self):
        
        if self.hunger > 10 or self.bored > 10 or self.poo_count > 10:
            return True
        elif self.hunger > 5 or self.bored > 5 or self.poo_count > 5:
            return True
        else:
            return False
        
    def worsen(self):
        
        action = random.randint(0,2)
        self.last_action = action

        if action == 0:
            self.hungry()
        elif action == 1:
            self.get_bored()
        elif action == 2:
            self.poo()

        
    # Positives
    def feed(self):
        self.hunger -= 1

    def play(self):
        self.boredness -= 1

    def clean(self):
        self.poo_count -= 1


    def determine_mood(self): # returns "happy", "mid", "sad"
        
        negativity = self.hunger + self.poo_count + self.bored

        if negativity <= 10:
            return HAPPY
        elif 20 > negativity > 10:
            return MID
        elif negativity > 20:
            return SAD

    def move(self):
        playeraction = confirm("Action", "What action to take?", buttons=["Feed", "Play", "Clean"])

        match playeraction:

            case "Feed":
                self.feed()
            case "Play":
                self.play()
            case "Clean":
                self.clean()
            


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
egg = Tamagotchi()

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