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
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #return colorList[random.randint(0, (len(colorList)-1))]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    while i <= 400:    
        pygame.draw.rect(screen, randColor(), (0+i/2,50+i/4,1,1+i), 0)
        i+=1
    pygame.draw.rect(screen, randColor(), (0+i/2,0+i/2,20+i,20+i/2), 0)
    
        
        
    clock.tick(60)#Only need 1 frame per second for a still image, increase for commented out draws on lines 38 & 39
    pygame.display.flip()
    