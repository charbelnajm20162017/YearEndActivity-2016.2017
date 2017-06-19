import pygame, random, sys

#Charbel Najm Dec 7 2016
colorList = [#these are used in the extra commented out lines below
    (0, 0, 0)
    ,(255, 255, 255)
    ,(0, 255, 0)
    ,(255, 0, 0)
    ,(0,0,255)
    ,(100,100,100)
    ,(200,200,200)
    ,(50,50,50)
    ,(20,20,20)
    ,(130,0,0)
    ,(0,130,0)
    ,(0,0,130)
    ]
pygame.init()
width = 510
screen = pygame.display.set_mode((width,800))

clock = pygame.time.Clock()

i = 0
screen.fill(colorList[1])

def randColor():
    return colorList[random.randint(0, (len(colorList)-1))]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    for i in range(0, 255):
        #pygame.draw.line(screen, randColor(), (i,0),(i,800),int(width/255))
        #pygame.draw.line(screen, randColor(), (i+255,0),(i+255,800),int(width/255))
        pygame.draw.line(screen, (i,0,100), (i,0),(i,800),int(width/255))
        pygame.draw.line(screen, (255-i,0,100), (i+255,0),(i+255,800),int(width/255))
        
    clock.tick(1)#Only need 1 frame per second for a still image, increase for commented out draws on lines 38 & 39
    pygame.display.flip()
    