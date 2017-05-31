import pygame as pg
import time as tt
import numpy as np
import math as mt
import random as rnd

x = pg.init()

clock = pg.time.Clock()



DspH = 600
DspW = 600
gd = pg.display.set_mode((DspW,DspH))

c = []

pink=(255,0,255)
aqua = (127,224,230)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
dgreen = (0,150,0)
blue = (0,0,255)
pink = (255,105,180)
dpink = (180,0,100)
orchid = (155,50,204)
sblue=(0,191,255)
dsblue = (30,4,200)
yellow = (255,255,0)
gold = (255,215,0)
orange = (255,127,0)

pg.mixer.music.load('sounds/title.wav')

hit  = pg.mixer.Sound('sounds/hit2.wav')
shoot  = pg.mixer.Sound('sounds/shoot.wav')
timer  = pg.mixer.Sound('sounds/timer.wav')
go  = pg.mixer.Sound('sounds/gameoverwav.wav')

img = pg.image.load('images/mytankcv.png')
tank1 = pg.image.load('images/tank1.png')
tank2 = pg.image.load('images/tank2.png')
tank3 = pg.image.load('images/tank3.png')
tank4 = pg.image.load('images/tank4.png')
pg.display.set_icon(img)


#pg.draw.rect(gd,red,[100,100,500,500])
q = True
shtrX = (DspW)/2
shtrY = DspH/2

def start():
    intro = True
    while intro:
        gd.fill(aqua)
        gd.blit(tank4,(10,20))
        gd.blit(tank3,(10,65))
        gd.blit(tank2,(10,110))
        gd.blit(tank1,(10,155))
        msg_to_scrn('<== 4 Points',red,-260,-210,Size= 20)
        msg_to_scrn('<== 3 Points',red,-215,-210,Size= 20)
        msg_to_scrn('<== 2 Points',red,-170,-210,Size= 20)
        msg_to_scrn('<== 1 Points',red,-125,-210,Size= 20)
        msg_to_scrn('Tank Strike',dsblue,-70,Size = 60,Font = 'comicsansms')
        msg_to_scrn('Shoot as much tank as  you can ',dpink,Size = 30,Font = 'comicsansms')
        msg_to_scrn('using "SPACE" In Thirty seconds.',dpink,50,Size = 30,Font = 'comicsansms')
        msg_to_scrn('Press "P" to start the game',black,140,Size = 30,Font = 'comicsansms')
        for et in pg.event.get():
            if et.type == pg.QUIT:
                quit()
            if et.type == pg.KEYDOWN:
                if et.key == pg.K_p:
                    gameloop(0)
                    intro = False
        pg.display.update()

def explode(x,y):
    expl = True
    while expl:
        xx = int(x)
        yy = int(y)
        for k in range(10):
            xe = int(rnd.randint(xx,xx+35))
            ye= int(rnd.randint(yy,yy+20))
            pg.draw.circle(gd,red,[xe,ye],6)
            pg.draw.circle(gd,yellow,[xe,ye],4)
        expl = False
def game_over(point):
    pg.mixer.music.stop()
    gameover = True
    x = 0
    gd.fill(orchid)
    while gameover:
        if x==0:
            pg.mixer.Sound.play(go)
        msg_to_scrn('TIMES UP',red,-60,Size = 60,Font = 'comicsansms')
        msg_to_scrn('Final Score: '+str(point),black,50,Size = 30,Font = 'comicsansms')
        msg_to_scrn('Play agian: "P"                 Quit: "Q"',black,120,Size = 27,Font = 'comicsansms')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type== pg.KEYDOWN:
                if event.key == pg.K_p:
                    start()
                    gameover = False
                if event.key == pg.K_q:
                    quit()
        x = 1
        pg.display.update()
def msg_to_scrn(msg,color,y_disp= 0,x_disp = 0,Font= 'Arial',Size=25):
    font = pg.font.SysFont(Font,Size)
    
    textS = font.render(msg,True,color)
    textrect = textS.get_rect()
    textrect.center = ((DspW/2)+x_disp),((DspH/2)+y_disp)
    gd.blit(textS,textrect)

def gameloop(minute=0):
    pg.mixer.music.play()
    Quit = False
    global shtrX
    global shtrY
    btX = 0
    btY = 0
    sX = 0
    sY = 0
    bX = 0
    bY = 0
    out = True
    w = 1
    first= []
    second = []
    third = []
    fourth = []
    FPS =   30
    minute = 0
    tcolor = blue
    ev=0
    point=0
    bsize = 10
    evilX = np.copy(DspW)
    evilY = np.copy(DspH)
    global q
    
    
    while not Quit :
        
        a = [12,6,4,3,2.4,2,1.74,1.5,1.33,1.2]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    sY = -5
                    sX = 0
                if event.key == pg.K_DOWN:
                    sY = 5
                    sX = 0
                if event.key == pg.K_RIGHT:
                    sX = 5
                    sY = 0
                if event.key == pg.K_LEFT:
                    sX = -5
                    sY = 0
                if event.key == pg.K_q:
                    quit()
                if event.key == pg.K_SPACE:
                    if btY< 0 or w == 1:
                        if out == True:
                            btX = np.copy(shtrX+20)
                            btY = np.copy(shtrY)
                            pg.mixer.Sound.play(shoot)
                            bY  = 0 
                            bY =-10
                            FPS = 30
                            w = 2
                    

        if shtrX > DspW-50:
            shtrX = DspW-49
        if shtrX <5:
            shtrX = 6
        if shtrY <DspH/2-1:
            shtrY =DspH/2+1
        if shtrY >DspH-50:
            shtrY =DspH-49
        shtrX += sX
        shtrY += sY
        
        
        btY += bY
        
        
        gd.fill(black,rect=[0,0,DspW,DspH/2])
        gd.fill(black,rect = [0,DspW/2,DspW,DspH])
        gd.fill(white,rect = [0,DspH/2-5,DspW,10])
        gd.blit(img,[shtrX,shtrY])
        pg.draw.ellipse(gd,red,[btX,btY,bsize,bsize])


        
        
        for i in a:
            if i in fourth:
                pass
            else:
                gd.blit(tank4,[evilX/i+15,evilY/12])
            
        for i in a:
            if i in third:
                pass
            else:
                gd.blit(tank3,[evilX/i,evilY/6])
            
        for i in a:
            if i in second:
               pass
            else:
                gd.blit(tank2,[evilX/i+15,evilY/4])
            
        for i in a:
            if i in first:
                pass
            else:
                gd.blit(tank1,[evilX/i,evilY/3])

        for i in a:
            if btX>(evilX/i) and btX<(evilX/i)+40:
                if btY>evilY/12 and btY < (evilY/12)+20 or btY+10>evilY/12 and btY+10<(evilY/12)+20:
                    if i in fourth:
                        pass
                    else:
                        pg.mixer.Sound.play(hit)
                        btY = -1
                        fourth.append(i)
                        point+=4
                        explode(evilX/i,evilY/12)
                if btY>evilY/6 and btY < (evilY/6)+20 or btY+10>evilY/6 and btY+10<(evilY/6)+20:
                    if i in third:
                        pass
                    else:
                        pg.mixer.Sound.play(hit)
                        btY = -1
                        third.append(i)
                        point+=3
                        explode(evilX/i,evilY/6)
                if btY>evilY/4 and btY < (evilY/4)+20 or btY+10>evilY/4 and btY+10<(evilY/4)+20:
                    if i in second:
                        pass
                    else:
                        pg.mixer.Sound.play(hit)
                        btY = -1
                        second.append(i)
                        point+=2
                        explode(evilX/i,evilY/4)
                if btY>evilY/3 and btY < (evilY/3)+20 or btY+10>evilY/3 and btY+10<(evilY/3)+20:
                    if i in first:
                        pass
                    else:
                        pg.mixer.Sound.play(hit)
                        btY=-1
                        first.append(i)
                        point+=1
                        explode(evilX/i,evilY/3)
                            
        ev+=1
        if ev%20==0:
            evilX -= 10
        else:
            evilX = DspW
        if ev%40==0:
            minute+=1
        msg_to_scrn('TIME: '+str(minute),tcolor,250,250)
        msg_to_scrn('POINTS: '+str(point),red,250,-250)
        if minute>24:
            tcolor = red
            if ev%40 == 0:
                pg.mixer.Sound.play(timer)
        if minute>30:
            game_over(point)
            sX=0
            sY=0
            bY=0
        pg.display.update()
        
        clock.tick(FPS)
    pg.quit()
    quit()

start()

    
