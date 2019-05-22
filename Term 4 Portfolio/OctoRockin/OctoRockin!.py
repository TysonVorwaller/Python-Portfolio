#OctoRockin!
#Tyson Vorwaller
#4/19


#imports
from superwires import games, color
import random



# global variables

games.init(screen_width = 640, screen_height = 480, fps= 60)

LIVES = 3
SCORE = 0



#classes

class  Octorock(games.Sprite):
    image = games.load_image("Images/octorock.jpg", transparent = True)

    def __init__(self, y = 60, speed = 5, odds_change = 33):
        super(Octorock,self).__init__(image = Octorock.image,
                                   x = games.screen.width/2,
                                   y = y,
                                   dx = speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()
        

    def check_drop(self):
        if self.time_til_drop > 0:

            self.time_til_drop -= 1
        else:
            new_boulder = Boulder(x = self.x)
            games.screen.add(new_boulder)
            self.time_til_drop = random.randint(60, 150)

class Link(games.Sprite):
    image = games.load_image("Images/link.jpg", transparent = True)

    def __init__(self):
        super(Link, self).__init__(image = Link.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)
    
    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        global SCORE
        for boulder in self.overlapping_sprites:
            SCORE += 10
            boulder.handle_caught()
            
        

class Boulder(games.Sprite):
    image = games.load_image("Images/boulder.jpg")
    speed  = random.randrange(4,10
                              )
    
    def __init__(self, x, y = 90, speed = random.randrange(speed)+1):
        super(Boulder,self).__init__(image = Boulder.image,
                                    x = x,
                                    y = y,
                                    dy = speed)
        

    def update(self):
        global LIVES
        if self.bottom > games.screen.height:
            self.destroy()
            LIVES -= 1
        if LIVES == 0:
            
            self.end_game()

    def end_game(self):
        """end the game"""
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

    def handle_caught(self):
        self.destroy()


class ScText(games.Text):
    def update(self):
        self.value = SCORE





#main
def main():
    
#   load data
##    start_image = games.load_image("Images/Title Screen.png", transparent = False)
##    input()
    wall_image = games.load_image("Images/zeldabackground.bmp", transparent = False)


#   create objects
    the_link = Link()
    the_octorock = Octorock()
    the_score = ScText(value = SCORE,
                   size = 60,
                   color = color.white,
                   x = 550,
                   y = 30)


#   draw
##    games.screen.title = start_image
##start = input("Hit Enter to Start")
##    if start != ("
##                 "):
##                 pass
    games.screen.background = wall_image
    games.screen.add(the_link)
    games.screen.add(the_octorock)
    games.screen.add(the_score)



#   game setup
    games.mouse.is_visible = False
    games.screen.event_grab = True


#   start loop
    games.screen.mainloop()




#starting point
main()
