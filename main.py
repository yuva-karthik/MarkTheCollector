import pygame as pyg
import random as rn
import math as mt 
import time as tm
#needed modules

pyg.init()
icon = pyg.image.load('gameIcon.png') 
p_avtr = pyg.image.load('mark.png')
c_avtr = pyg.image.load('dollar.png')
bg = pyg.image.load('grassbg.jpg')
bmb_avtr = pyg.image.load('bomb.png')
font = pyg.font.Font('Bear-Hug.ttf',32)
#render images and fonts

class window:
    def __init__(self, wn, title, logo):
        self.wn = pyg.display.set_mode((800,600))
        self.title = pyg.display.set_caption("Mark the collector")
        self.logo = pyg.display.set_icon(icon)

screen = window("page","head","gameIcon")
s1 = screen.wn
#display setup

class avatar:
    def player(a,b):
     s1.blit(p_avtr,(a,b))

pX = 400
pY = 300
pX_change = 0
pY_change = 0
#player setup

class dollar:
    def coin(d,c):
        s1.blit(c_avtr,(d,c))

cX = rn.randint(0,738)
cY = rn.randint(60,538)
#coin setup

class bomb:
    def nuke(e,f):
        s1.blit(bmb_avtr,(e,f))

bX = rn.randint(80,738)
bY = rn.randint(80,518)
#bomb setup

def collect(b1,b2,b3,b4):
    x = abs(b1 - b3)
    y = abs(b2 - b4)
    dist = mt.sqrt(mt.pow(x,2) + mt.pow(y,2))
    if dist < 35:
        return True
    else:
        return False
#pickup function    

def pos(b1,b2,b3,b4):
    x = abs(b1 - b3)
    y = abs(b2 - b4)
    dist = mt.sqrt(mt.pow(x,2) + mt.pow(y,2))
    if dist < 64:
        return True
    else:
        return False
#coin and bomb uncertainity
    
def doom(b1,b2,b3,b4):
    x = abs(b1 - b3)
    y = abs(b2 - b4)
    dist = mt.sqrt(mt.pow(x,2) + mt.pow(y,2))
    if dist < 35:
     return True
    else:
     return False
#eplosion function
    
def swt(a):
    if a%2 == 0 or a%3 == 0:
        return True
#bomb position change function 

score = 0
tX = 300
tY = 10
def points(x,y):
    scr = font.render('SCORE: ' + str(score), True, ('yellow'))
    s1.blit(scr,(x,y))
#score card function

mX = 260
mY = 300
def msg(x,y):
    gmsg = font.render('<--GAME OVER-->', True, ('green'))
    s1.blit(gmsg,(x,y))
#end game statement function

rX = 350
rY = 300
def pmsg(x,y):
   lag = font.render('PAUSE', True, ('blue'))
   s1.blit(lag,(x,y))
#pause game statement function
                     
run = True 
move = 0.3
cont = False
play = True
hold = False
#variables for mainloop 

#main loop
while run:
    s1.fill('black')
    s1.blit(bg,(0,0))
    #screen loop

    #keyboard binding
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
        #pause func
        if event.type == pyg.KEYDOWN:
            if hold == False:
             if event.key == pyg.K_SPACE:
                hold = True
                pX_change = 0
                pY_change = 0
                break
            if hold == True:
             if event.key == pyg.K_SPACE:
                hold = False 
            #movement func
            if play and hold == False:
             if event.key == pyg.K_UP or event.key == pyg.K_w:
                pY_change = -move
             if event.key == pyg.K_DOWN or event.key == pyg.K_s:
                pY_change = move
             if event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                pX_change = move
             if event.key == pyg.K_LEFT or event.key == pyg.K_a:
                pX_change = -move
    #boundaries
    if pX <= 0:
        pX = 0
    elif pX >= 738:
        pX = 738
    if pY <= 60:
        pY = 60
    elif pY >= 538:
        pY = 538
        
    #move 
    pX += pX_change
    pY += pY_change

    #calling the functions
    collect(pX,pY,cX,cY)
    take = collect(pX,pY,cX,cY)
    doom(pX,pY,bX,bY)
    blst = doom(pX,pY,bX,bY)
    pos(bX,bY,cX,cY)
    chnge = pos(bX,bY,cX,cY)

    dollar.coin(cX,cY)
    bomb.nuke(bX,bY)
    avatar.player(pX,pY)
    points(tX,tY)

    if hold:
       pmsg(rX,rY)

    if take:
        tm.sleep(0.02)
        cX = rn.randint(0,738)
        cY = rn.randint(60,538)
        score += 1
        if swt(score):
         bX = rn.randint(0,738)
         bY = rn.randint(80,518)
        if score%12 == 0:
         move += 0.1
    if chnge:
        bX = rn.randint(0,738)
        bY = rn.randint(80,518)
    if blst:
        cont = True
    if cont:
        msg(mX,mY)
        play = False
        pX_change = 0
        pY_change = 0
    
    pyg.display.flip()

pyg.quit()