# Build a screen and a moving block

'''import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        pass

    def run(self):
            surface = pygame.display.set_mode((500, 500))

        
class snake:
    def __init__(self,parent_screen):
       self.parent_screen = parent_screen
       self.block = pygame.image.load("block.jpg").convert()

    self.x, self.y = 100, 100

    def draw(self):
     self.parent_screen.fill((110, 110, 5))
     self.parent_screen.blit(block, (block_x, block_y))
    #to display in screen
    pygame.display.flip()

def draw_block():
    # for color background
    
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    #background color
    surface.fill((110, 110, 5))
# for block image
    
    block = pygame.image.load("block.jpg").convert()

    block_x, block_y = 100, 100
# block ki position 
    surface.blit(block, (block_x, block_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    #for movement of block screen p upar niche daye bayen
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                    
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()

            elif event.type == QUIT:
                running = False'''
# Make it all object oriented by converting the code in various classes

'''import pygame
from pygame.locals import *
import time
class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("block.jpg").convert()

        self.x = 100
        self.y = 100
        self.direction = 'up'
    def draw(self):
        self.parent_screen.fill((110, 110, 5))

        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()


    def move_left(self):
        self.direction = 'left'
        

    def move_right(self):
        self.direction = 'right'
       
    def move_up(self):
        self.direction = 'up'
        
    def move_down(self):
        self.direction = 'down'
        

   

#if its moving down go down if up go up
def walk(self):
        if self.direction == 'left':
            self.x -= 10
        elif self.direction == 'right':
            self.x += 10
        elif self.direction == 'up':
            self.y -= 10   
        elif self.direction == 'down':
            self.y += 10

            self.draw()  # Redraw the snake at the new position
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

                    self.snake.walk()
                    #for speed of block kitne teej bhage
            time.sleep(0.2)

if __name__ == '__main__':
    game = Game()
    game.run()'''
# Moving block with a timer

'''import pygame
from pygame.locals import *
import time

class Snake:
    # snake ki length badhde uske liye lenghth add kri
    def __init__(self, surface,length):
        self.parent_screen = surface
        self.block = pygame.image.load("block.jpg").convert()

        self.length = length  # Length of the snake
        self.x = [40]*length
        self.y = [40]*length
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'left':
            self.x[0] -= 10
        if self.direction == 'right':
            self.x[0] += 10
        if self.direction == 'up':
            self.y[0] -= 10
        if self.direction == 'down':
            self.y[0] += 10

        self.draw()


    def draw(self):
        self.parent_screen.fill((110, 110, 5))

        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface,2)  # Initialize snake with a length of 2
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()

            time.sleep(.2)

if __name__ == '__main__':
    game = Game()
    game.run()
'''

'''import pygame
from pygame.locals import *
import time
import random

SIZE = 40
#class for apple
# apple ki position random ho jaye
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        #blit se object draw hote hai
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)*SIZE
        self.y = random.randint(1,20)*SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.direction = 'down'

        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()


    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(.2)

if __name__ == '__main__':
    game = Game()
    game.run()'''


'''import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()  # fixed name
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 24) * SIZE
        self.y = random.randint(0, 19) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("block.jpg").convert()  # fixed name
        self.direction = 'down'
        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake(self.surface, 5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        return x1 == x2 and y1 == y2

    def play(self):
        self.snake.walk()
        self.apple.draw()

        # check collision with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            for i in range(self.snake.length):
                # check if snake collides with itself
                if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x,self.apple.y):
                    self.apple.move() 
            #jabh apple khaye to bada ho jaye saap
        def is_collision(self, x1, y1, x2, y2):
            if x1>=x2 and x1<=x2+SIZE:
                if y1>=y2 and y1<=y2+SIZE:
                    return True
            return False



    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(.2)


if __name__ == '__main__':
    game = Game()
    game.run()'''
# Write logic for snake eating apple and display score

'''import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)*SIZE
        self.y = random.randint(1,20)*SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.direction = 'down'

        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
# score show karne ke liye
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(.2)

if __name__ == '__main__':
    game = Game()
    game.run()
'''
'''import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()  # fixed variable name
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 25) * SIZE
        self.y = random.randint(1, 20) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("block.jpg").convert()  # fixed variable name
        self.direction = 'down'
        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length - 2}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # collision with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
        #collision with sanke itself khud se takra jaye toh game over kese ho
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise'tu maar gya khatam,ja dubara khel'
                

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False
                              
             self.play()
            time.sleep(0.2)


if __name__ == '__main__':
    game = Game()
    game.run()'''
# Game over scenario and pausing a game

'''import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Codebasics Snake And Apple Game")
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
# dubara shuru se start ho naye score k sath
    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occured"

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        # to show msg 
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            # enter dabane p naya game start ho jaye
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                #pause krne k liye
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)

if __name__ == '__main__':
    game = Game()
    game.run()
'''
'''import pygame
from pygame.locals import *
import time
import random

SIZE = 40
#BACKGROUND_COLOR = (110, 110, 5) no used as we render background separately

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()  # fixed
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("block.jpg").convert()  # fixed
        self.direction = 'down'
        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()
        # background m photo geri h yaha p
    def render_background(self):
        bg = pygame.image.load("background.jpg").convert()
        self.parent_screen.blit(bg, (0, 0))

    def draw(self):
        #self.parent_screen.fill(BACKGROUND_COLOR)   not needed as we render background separately
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
       # self.play_background_music()
        pygame.display.set_caption("Snake and Apple Game")
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    #baackground music play karne k liye main h
    def play_background_music(self):
        pygame.mixer.music.load('')
        pygame.mixer.music.play(-1,0)

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            #to add sound when snake eats apple main chij
            sound=pygame.mixer.Sound('cat.mp3')
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                #marane p awaj kesi ayegi
                sound = pygame.mixer.Sound('dog.mp3')
                pygame.mixer.Sound.play(sound)
                raise Exception("Collision Occured")

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        #self.surface.fill(BACKGROUND_COLOR) no used as we render background separately
        self.snake.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"tu maar gya khatam Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("ja dubara khel", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()
        pygame.mixer.music.pause()  # Stop background music on game over

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()  # marne k baad shuru se music chale
                        pause = False
                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.25)


if __name__ == '__main__':
    game = Game()
    game.run()
'''
# we use pygame as a library
import sys, os, pygame, time, random
from pygame.locals import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # When running in .exe
    except Exception:
        base_path = os.path.abspath(".")  # When running in .py
    return os.path.join(base_path, relative_path)

# size of snake/apple block
SIZE = 40
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(resource_path("apple.jpg")).convert()  # load apple image
        self.x = 120  # initial X
        self.y = 120  # initial Y

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))  # draw apple
        pygame.display.flip()  # to update the display

    def move(self):
        # move apple randomly on screen
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(resource_path("block.jpg")).convert()  # block image load karte hai
        self.direction = 'down'  # initial direction
        self.length = 1  # initial length
        self.x = [40]  # snake ki position X
        self.y = [40]  # snake ki position Y

    # snake ko left move karne ke liye
    def move_left(self):
        self.direction = 'left'

    # snake ko right move karne ke liye
    def move_right(self):
        self.direction = 'right'

    # snake ko up move karne ke liye
    def move_up(self):
        self.direction = 'up'

    # snake ko down move karne ke liye
    def move_down(self):
        self.direction = 'down'

    # snake ka body update karne ke liye
    def walk(self):
        # update snake body positions (from tail to head)
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head position
        # snake k sarir ke hisab se head position update karte hai
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        # render background and draw snake
        # render matlab draw karna or display karna
        self.render_background()
        self.draw()

    # background image render
    def render_background(self):
        bg = pygame.image.load(resource_path("background.jpg")).convert()
        self.parent_screen.blit(bg, (0, 0))

    # snake ki body draw karte hai
    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    # increase snake length when it eats apple
    def increase_length(self):
        self.length += 1
        self.x.append(-1)  # dummy coordinate
        self.y.append(-1)  # dummy coordinate

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_background_music()  # background music start
        pygame.display.set_caption("Snake and Apple Game")
        self.surface = pygame.display.set_mode((1000, 800))  # game window

        # snake and apple init
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    # reset the game state
    # jab game khatam ho jaye to reset karte hai
    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    # sanke aur apple ke beech collision check karte hai
    def is_collision(self, x1, y1, x2, y2):
        # agar snake aur apple ke beech collision ho jaye to snake length increase karte hai
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    # background music play karne ke liye
    def play_background_music(self):
        pygame.mixer.music.load(resource_path("naagin.mp3"))
        pygame.mixer.music.play(-1, 0)  # loop infinite

    # in sabh ka matlab hai ki moves the snake, shows the apple, shows the score, then updates the screen.
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()

        font = pygame.font.SysFont('arial', 20)  # choose font and size
        msg = font.render("Aryan's Snake Game 🐍 – Stay sharp!", True, (255, 255, 0))
        self.surface.blit(msg, (10, 770))  # position text at bottom-left of window
        pygame.display.flip()

        # Apple collision
        # agar snake ka head apple ke sath collide ho jaye to snake ki length increase
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            # khane p sound aayegi
            sound = pygame.mixer.Sound(resource_path("cat.mp3"))  # play sound when snake eats apple
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.apple.move()

        # Snake body collision
        # snake apne se collide kre toh woh maar jaye or game over ho jaye
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                # jab snake apne se takra jaye to sound aayegi
                sound = pygame.mixer.Sound(resource_path("super.mp3"))
                pygame.mixer.Sound.play(sound)
                raise Exception("Collision Occured")

        # Wall collision check (new)
        if (self.snake.x[0] < 0 or self.snake.x[0] >= 1000 or# beyond width
            self.snake.y[0] < 0 or self.snake.y[0] >= 800):# beyond height
            sound = pygame.mixer.Sound(resource_path("super.mp3"))
            pygame.mixer.Sound.play(sound)
            raise Exception("Wall Hit")

    # score display karne ke liye
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length - 1}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.snake.render_background()
        font = pygame.font.SysFont('arial', 30)

        # motivational + score
        line1 = font.render(f"Game Over  'Every failure is a step to victory'. Try again! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))

        line2 = font.render("Every pro was once a beginner — try again!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        # --- Custom tagline on game over screen ---
        tagline = font.render("Aryan's Snake Game 🐍 – Thanks for playing!", True, (255, 255, 0))
        self.surface.blit(tagline, (650, 15))
        pygame.display.flip()

        pygame.display.flip()
        pygame.mixer.music.pause()

    def run(self):
        running = True
        pause = False

        # game chalane ke liye loop jabh tak game chal raha hai or ho quit na kre
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:  # ESC to quit
                        running = False
                    if event.key == K_RETURN:  # ENTER to restart
                        pygame.mixer.music.stop()  # stop old music
                        pygame.mixer.music.play(-1, 0.0)  # play again from start
                        pause = False

                    if not pause:  # movement allowed only when game is not paused
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:  # quit if X button pressed
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception:
                # game over scenario
                self.show_game_over()
                pause = True  # pause game
                self.reset()  # enter marte p game reset ho jaye

            time.sleep(0.25)  # speed of snake

if __name__ == '__main__':
    game = Game()  # Initialize the game
    game.run()     # Start the game loop
