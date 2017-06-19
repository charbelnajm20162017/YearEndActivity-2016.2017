import pygame, random, sys
import WordpressScraper as ws

#dimensions
width = 800
height = 800
#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
GREEN1 = (17,180,0)
GREEN2 = (10,160,0)
BLUE = (0,0,255)
GREY = (120,120,120)
BROWN = (120,50,0)

#this list holds all the base urls to scan
siteList = ["https://pmssdm2016.wordpress.com",
            "https://pmsscoding2016.wordpress.com",
            "https://pmssanimation2016.wordpress.com",
            "https://pmssict2016.wordpress.com",]

#grab data using WordpressScraper module
countData = ws.getData(siteList)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.init()
headerFont = pygame.font.Font(pygame.font.get_default_font(), 15)

#divide the screenspace into 4 quadrants
vQuadrants = height / (len(countData) /2)
hQuadrants =  width / (len(countData) /2)

class quadrant:
    def __init__(self, x, y, t, h):
        self.x, self.y, self.t, self.h = x, y, t, h
    #stores the position of the quadrant rect
    def pos(self):
        return (self.x, self.y, self.t, self.h)
    #stores/links a pygame rect to a class instance variable
    def link(self, rect):
        self.rect = rect
    #this holds all the quadrant's metadata
    def metaData(self, headerUrl, artCount):
        self.headerUrl = headerUrl
        self.artCount = artCount
        
#create a class instance for each quadrant and give each a position
q1 = quadrant(1, 1, ((width/2)-5), ((height/2)-5))
q2 = quadrant(q1.t+5, 1, ((width/2)-1), ((height/2)-5))
q3 = quadrant(1, (height/2), ((width/2)-5), ((height/2)-5))
q4 = quadrant(q3.t+5, (height/2), ((width/2)-1), ((height/2)-5))

#take the data to be visualized and assign each to a quadrant
if len(countData) >= 5:
    raise OverflowError("Stopping: imported data exceeds displaying capability")
else:
    # "unzip" the dictionary into 2 lists.
    keys0 = list(countData.keys())
    values0 = list(countData.values())
    for l in range(len(countData)):
        if l == 0:
            q1.metaData(keys0[l], values0[l])
        if l == 1:
            q2.metaData(keys0[l], values0[l])
        if l == 2:
            q3.metaData(keys0[l], values0[l])
        if l == 3:
            q4.metaData(keys0[l], values0[l])
            
#Main Pygame Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #Grey BG color
    screen.fill((200,200,200))
    
    #Link the quadrant rects to their respective class instance 
    q1.link(pygame.draw.rect(screen, GREY, q1.pos()))
    q2.link(pygame.draw.rect(screen, GREY, q2.pos()))
    q3.link(pygame.draw.rect(screen, GREY, q3.pos()))
    q4.link(pygame.draw.rect(screen, GREY, q4.pos()))
    
    # Trees!
    
    def treeify(quadrant, seed):
        global posPrev, pos
        branchList = []
        i = 20
        #DRAW Trunk. Larger seeds will make the tree taller.
        for i in range(0, i):
            xJitter = random.randint(-5,5)
            yTravel = random.randint(-5,5)
            pos = (quadrant.rect.center[0]+(xJitter), (quadrant.rect.bottom-(15*i)-int(seed*1.14)))
            #print("iteration ",i," ", pos) #For debugging
            if quadrant == q3 or quadrant == q4:
                pos = (quadrant.rect.center[0]+(xJitter), quadrant.rect.bottom-(15*i)-int(seed*1.14))
                pygame.draw.line(screen,BROWN, (quadrant.rect.center[0], quadrant.rect.bottom-5), (pos), 4) ##
            else:
                pygame.draw.line(screen,BROWN, (quadrant.rect.center[0], quadrant.rect.h-5), (pos), 4) ##
        #DRAW Branch(es)
        for s in range(0, seed):
            xJitter = random.randint(-5,5)
            yTravel = random.randint(-5,5)            
            branch = random.randint(pos[1], (quadrant.rect.bottom-100)) #Specify a range on the trunk to add branches
            #Add jitter to the branches 
            b = pygame.draw.line(screen, GREEN1, (pos[0], branch),  ((pos[0]+ 60 + yTravel - xJitter),branch - yTravel ), 4)
            b1 = pygame.draw.line(screen, GREEN2, (pos[0], branch), ((pos[0]- 55 + yTravel - xJitter),branch - yTravel ), 4)
            branchList.append(b.size)
            
            
    #an unused trunk drawing method kept for reference, this trunk will progressively get thinner.
    def treeify2(quadrant, seed):
        global posPrev, pos
        branchList = []
        i = 20
        for i in range(1, i):
            #xJitter = random.randint(-int(quadrant.rect.w/2),int(quadrant.rect.w/2))
            xJitter = random.randint(-5,5)
            yTravel = random.randint(-5,5)
            pos = (quadrant.rect.center[0]+(xJitter), quadrant.rect.h-(15*i+xJitter))
            #print("iteration ",i," ", pos)
            trunk = pygame.draw.line(screen,BLUE, (quadrant.rect.center[0], quadrant.rect.h-5), (pos), int(80-i*4))    
    
    #Quadrant headers
    hq1 = headerFont.render("{} :{}".format(q1.headerUrl, q1.artCount), 1, WHITE)
    hq2 = headerFont.render("{} :{}".format(q2.headerUrl, q2.artCount), 1, WHITE)
    hq3 = headerFont.render("{} :{}".format(q3.headerUrl, q3.artCount), 1, WHITE)
    hq4 = headerFont.render("{} :{}".format(q4.headerUrl, q4.artCount), 1, WHITE)
    
    #Call the trees!
    treeify(q1, q1.artCount)
    treeify(q2, q2.artCount)
    treeify(q3, q3.artCount)
    treeify(q4, q4.artCount)
    
    screen.blit(hq1, (q1.rect.topleft))
    screen.blit(hq2, (q2.rect.topleft))
    screen.blit(hq3, (q3.rect.topleft))
    screen.blit(hq4, (q4.rect.topleft))
    
    clock.tick(12)#increase this for faster animation
    pygame.display.flip()
    
    #comment out the lines below to enable animation
    #pygame.quit()
    #sys.exit()    
    