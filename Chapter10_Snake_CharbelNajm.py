import pygame, random, sys

width = 300
height = 300

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake-Charbel Najm")
clock = pygame.time.Clock()
pygame.init()

class snake(object):
    def __init__(self, x, y, size=10, color=WHITE):
        self.x = x
        self.y = y

#snake vars
xspeed = 0
yspeed = 0
xpos = 1
ypos = 1
spacing = 3
direction = "none"
snakeBody = []
snakeSize = 2
foods = []
pygame.key.set_repeat(1, 30)

def genFood(xy, color=GREEN, foodSize=(5,5)):
    print(xy)
    x1 = xy[0]
    y1 = xy[1]
    foodRect = pygame.draw.rect(screen, color, (x1, y1, 5,5))
    foods.append(foodRect)

snakeBody.append(snake(0,0))
genFood((50,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if direction == "DOWN":#to prevent going in the opposite direction
                    break
                direction = "UP"
                xspeed = 0
                yspeed = (10 + spacing)*-1
                xpos = xspeed + xpos
                ypos = yspeed + ypos
                snakeBody.append(snake(xpos,ypos))     
                
            if event.key == pygame.K_DOWN:
                if direction == "UP":
                    break                
                direction = "DOWN"
                xspeed = 0
                yspeed = 10 + spacing
                xpos = xspeed + xpos
                ypos = yspeed + ypos
                snakeBody.append(snake(xpos,ypos))    
                
            if event.key == pygame.K_RIGHT:
                if direction == "LEFT":
                    break
                direction = "RIGHT"
                yspeed = 0
                xspeed = 10 + spacing
                xpos = xspeed + xpos
                ypos = yspeed + ypos
                snakeBody.append(snake(xpos,ypos))      
                
            if event.key == pygame.K_LEFT:
                if direction == "RIGHT":
                    break                
                direction = "LEFT"
                yspeed = 0
                xspeed = (10 + spacing)*-1
                xpos = xspeed + xpos
                ypos = yspeed + ypos
                snakeBody.append(snake(xpos,ypos))
                
        if pygame.mouse.get_pressed() == (1,0,0):
            print("pressed")
            genFood(pygame.mouse.get_pos())

    #Wrap around            
    if(xpos >= 300):
        xpos = 1
    elif(xpos <= 0):
        xpos = 299

    if(ypos >= 300):
        ypos = 1
    elif(ypos <= 0):
        ypos = 299
        
    screen.fill(BLACK)
    if len(snakeBody) >= snakeSize:
        snakeBody.pop(0)
    for i in snakeBody:
        snakeHead = pygame.draw.rect(screen, WHITE, (i.x, i.y, 10,10))    
    for i in foods:
        pygame.draw.rect(screen, GREEN, (i.x, i.y, 5,5))
    #collision detection (in actuality is position checking rather than collision detection)
        if (snakeHead.x <= (i.x + 10) and snakeHead.x >= (i.x - 10) and snakeHead.y <= (i.y + 10) and snakeHead.y >= (i.y - 10)):#+10 to make it easier to grab
            print("HIT")
            foods.remove(i)
            snakeSize += 1
    
    clock.tick(60)
    pygame.display.flip()
