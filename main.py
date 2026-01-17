import pygame
from pygame.locals import *
from threading import Thread
import time
import queue
import sys

# self coded classes
import ActionHandler

running = True
keyQueue = queue.Queue()
gameState = queue.Queue()

class Logic(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        global running
        actionHandler = ActionHandler()
        actionHandler.readConfig()
        while running:
            for entity in entityList:
                if entity.controllable == True:
                    #wait for keyaction
                else:
                    entitiy.aimove()
            # get the action
            while not keyQueue.empty():
                actionHandler.execute(keyQueue.get())
            time.sleep(0.01)



def main():
    pygame.init()
    global running
    canvas = pygame.display.set_mode((300,300))
    LogicThread = Logic()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                keyQueue.put(event.key)
            pygame.display.update()
        stonetile = pygame.image.load("stone_tile.png").convert()
        canvas.blit(stonetile, (0, 0))
    LogicThread.join()
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
