import pygame, sys
import time

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()  # START HERE_____________________________________________________
pygame.display.set_caption('DXBALL EXTENDED v1.2!')
# __________________________________________________________TEXT
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
myfont = pygame.font.SysFont("comicsansms", 72)
myfont2 = pygame.font.SysFont("comicsansms", 36)
text_gameover = myfont.render('TRY AGAIN!', True, (0,128,0))
text_win=myfont.render('OK YOU WIN!', True, (0,128,0))
text_start=myfont2.render('PRESS MOUSE TO START!', True, (0,128,0))
textRect = text_gameover.get_rect()
# _________________________________________________________
pygame.mouse.set_cursor(*pygame.cursors.diamond)
RANGEX, RANGEY = 10, 5
corr = 700
SPEEDCONTROL = 250
window = pygame.display.set_mode((corr, corr))
textRect.centerx = window.get_rect().centerx    #Text coor
textRect.centery = window.get_rect().centery    #Text coor
pygame.mixer.music.load('bat.mp3')

pygame.mixer.music.load('pad.mp3')

padding=pygame.image.load("padding.png")
backg = pygame.image.load("backg.jpg")
ballimage = pygame.image.load("ball.png")
padimage = pygame.image.load("pad.png")
batimage = pygame.image.load("bat.png")
xpad, ypad = corr/2, corr-100
xbal, ybal = 100, 250
time1 = pygame.time.Clock()
key, kay = True, True
timel = time1.tick(100)
secondsx = timel * SPEEDCONTROL / 1000.0
secondsy = timel * SPEEDCONTROL / 1000.0


def move_condition(xbal, ybal, xtarget, ytarget, htarget, wtarget):
    global secondsx
    global secondsy
    condition = 0
    if xtarget <= xbal + 12 <= xtarget + wtarget and ytarget <= ybal + 24 <= ytarget + 5:
        #print ("ÜST")
        condition = 1  # üst
        ybal -= 10
        if wtarget == 128: # if its PAD
            if 0 < xbal+12 < xtarget + wtarget/4 and secondsx > 0: # sol 1/4
                print ("1-4 BOLGEEE")
                secondsx=-secondsx-5
            if xtarget + wtarget/4 <=xbal+12 <= xtarget + wtarget/2 and secondsx > 0: # sağ yarim
                print ("2-4 BOLGEEE")
                secondsx=-secondsx+5
            if xtarget+wtarget/2 < xbal+12 < xtarget + wtarget*3/4 and secondsx < 0: # sağ yarim
                print ("3-4 BOLGEEE")
                secondsx=-secondsx-5
            if xtarget + wtarget*3/4 <= xbal+12 <= xtarget + wtarget and secondsx < 0: # sağ tam
                secondsx=-secondsx+5
                print ("4-4 BOLGEEE")
        secondsy =-secondsy
    elif xtarget <= xbal + 12 <= xtarget + wtarget and ytarget + htarget - 5 < ybal < ytarget + htarget:
        #print ("ALT")
        condition = 2  # alt
        ybal += 10
        secondsy = -secondsy
    elif ytarget+5 <= ybal+12 <= ytarget + htarget-5 and xtarget < xbal + 18 < xtarget + 5:
        #print ("SOL")
        condition = 3  # sol
        xbal -= 10
        secondsx = -secondsx
    elif ytarget+5 <= ybal+12 <= ytarget + htarget-5 and xtarget + wtarget - 5 < xbal < xtarget + wtarget+5:
        #print("SAĞ")
        condition = 4  # sağ
        xbal += 10
        secondsx = -secondsx
    else:
        pass
    return condition

bats = [[1 for x in range(RANGEX)] for x in range(RANGEY)]

window.blit(text_start, textRect)
pygame.display.update()
time.sleep(1.0)

while 1:
    for press in pygame.event.get():
        if press.type== pygame.MOUSEBUTTONUP:
            counter=(RANGEX-1)*(RANGEY-1)
            while 1:
            # ______________________________________________________________________________STARTING MAIN LOOOOOOOOOOOOOOOP
                window.blit(backg, (0, 0))
                window.blit(ballimage, (xbal, ybal))
                window.blit(padimage, (xpad, ypad))
                window.blit(padding,(0,0))
                window.blit(pygame.transform.rotate(padding,180),(647,0))
                """xbal += secondsx
                ybal += secondsy"""
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        xbal,ybal=pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
                # _____________________________________________________________________________________________BAT GOSTERİM
                for a in range(1, RANGEX):
                    for b in range(1, RANGEY):
                        if bats[b][a] != 0:
                            window.blit(batimage, (a * 60, (b+1) * 20))
                pygame.display.update()
                # _____________________________________________________________________________________________BAT KAYİT
                for k in range(0, RANGEX):
                    for m in range(0, RANGEY):
                        if bats[m][k]==1 and move_condition(xbal, ybal, k * 60, (m+1) * 20, 20, 60) != 0:
                            pygame.mixer.music.play(0)
                            bats[m][k] = 0
                            counter-=1

                            if counter==0:
                                counter=(RANGEX-1)*(RANGEY-1)
                                window.blit(text_win, textRect)
                                pygame.display.update()
                                time.sleep(1.5)
                                bats = [[1 for x in range(RANGEX)] for x in range(RANGEY)]

                # ___________________________________________________________________________________________PAD HAREKETİ
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        xpad=pygame.mouse.get_pos()[0]-64
                if(move_condition(xbal, ybal, xpad, ypad, 30, 128)):  # PAD MOVE
                    pygame.mixer.music.play()
                # _________________________________________________________________________________________TOP DİŞARİ ÇİKMA
                if xbal <= 53 :
                    secondsx = -secondsx
                    xbal+=10
                elif xbal+24 >= corr - 53:
                    secondsx = -secondsx
                    xbal-=10
                else:
                    pass
                if ybal <= 5 or ybal >= corr - 25:
                    if ybal>= corr-25:#_______________________________________________________________U LOSE TRY AGAIN TEXT
                        window.blit(text_gameover, textRect)
                        pygame.display.update()
                        time.sleep(1.5)
                        xbal,ybal=xpad+60,ypad-25
                        secondsx = timel * SPEEDCONTROL / 1000.0
                        secondsy = timel * SPEEDCONTROL / 1000.0
                        secondsy=-secondsy
                    else:
                        secondsy = -secondsy

            pygame.display.update()
pygame.quit()  #__________________________________________   END HERE__________________________________________________
