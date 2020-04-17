print(__name__)

#standard exit code to prevent use as a program
if __name__ == '__main__':
    errormessage = 'This is a module and should not be run alone'
    print(errormessage)
    #quits if run as script
    from sys import exit
    exit(errormessage)

#------------------------------------------------

#onze eigen code
from .world import player, enemies, objects
from .UI import klok
from . import settings, levelcreator, globale_variablen as glob, camera, gfx

from time import sleep

#andere shit die geimporteerd moet worden
import pygame

#this wil initialize the game loop
def start():
    #pygame
    pygame.init()
    global clock
    clock = pygame.time.Clock() 
    
    #sytze's stopwatch
    global stopwatch
    stopwatch = klok.stopwatch((0,255,0),(255,255,255),820,5,True,True,5,(0,0,0))
    
    #creation
    levelcreator.createlevel('level_2.png')
    print(glob.allCollisionObjects)
    
    #firstdraw
    glob.screen.fill(settings.background_color)
    pygame.display.update()
    
counter = 0
   

#this is what is executed every tick
def loop():
    #predraw
    for each in glob.allCollisionObjects:
        each.predraw()
    glob.ragnar.predraw()
    
    #camera
    camera.cameramovement()

    #player
    keys = pygame.key.get_pressed()
    glob.ragnar.horizontalmovement(keys)
    glob.ragnar.verticalmovement(keys)
    inrange = glob.ragnar.get_inrange()
    glob.ragnar.collision(inrange)
    glob.ragnar.gravity(inrange)
    
    #postdraw
    for each in glob.allCollisionObjects:
        each.postdraw()
    glob.ragnar.postdraw()
    
    pygame.display.update()
    
    #misc
    stopwatch.update()
    global counter
    counter += 1
    if counter > 120:
        counter = 0
        print(clock.get_fps() )
    
    #code om het script te stoppen
    for event in pygame.event.get():        #haalt alle events op. een van de events is het drukken op kruisje
        if event.type == pygame.QUIT:       #als op het kruisje is gedrukt
            glob.running = False                  #dan sluit pygame af 
    
    #clock tic gaat als laatste omdat deze wacht als we te snel zijn gegaan
    clock.tick(settings.gamespeed)
    

            
            
            
#dit is opruimcode 
#AKA de allobject lijst moet geleegd en alle refrences naar start variablen moeten verwijderd 
def end():
    glob.allCllisionObjects.clear()
    glob.ragnar = 0 

    pygame.quit()