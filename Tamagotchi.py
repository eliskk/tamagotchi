HAPPY = ".\\gfx\\faces\\happy.png"
MID = ".\\gfx\\faces\\gfx\\mid.png"
SAD = ".\\gfx\\faces\\gfx\\sad.png"
DEAD = ".\\gfx\\faces\\gfx\\dead.png"
POO = ".\\gfx\\faces\\gfx\\poo.png"            

from random import randint
from pyautogui import confirm


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
        
        action = randint(0,2)
        self.last_action = action

        match action:
            case 0:
               self.hungry()
            case 1:
                self.get_bored()
            case 2:
                self.poo()            

        
    # Positives
    def feed(self):
        if self.hunger <= 0: 
            pass
        else:
            self.hunger -= 1

    def play(self):
        if self.bored <= 0:
            pass
        else:
            self.bored -= 1

    def clean(self):
        if self.poo_count <= 0:
            pass
        else:
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