import pygame
from pygame.locals import *
from threading import Thread
import time
import queue
import sys


# self coded classes
import actionhandler
import gameobjects

running = True
keyQueue = queue.Queue()
gameState = queue.Queue() 

entityList = []

class Logic(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        global running
        actionHandler = actionhandler.ActionHandler()
        actionHandler.readConfig()
        while running:
#            for entity in entityList:
#                if entity.controllable == True:
#                    #wait for keyaction
#                else:
#                    entitiy.aimove()
            # get the action
            while not keyQueue.empty():
                actionHandler.execute(keyQueue.get())
            time.sleep(0.1)

class LevelStructure():
    def __init__(self, filename):
        self.walls = []
        with open(filename, "r") as f:
            row = 0
            for line in f:
                column = 0
                for char in line:
                    if char == "#":
                        self.walls.append(gameobjects.Structure(column, row, "stone_tile.png", True))
                    column+=1
                row+=1

def main():
    pygame.init()
    global running
    canvas = pygame.display.set_mode((960,640))
    LogicThread = Logic()
    levelStructure = LevelStructure("bana.map")
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                keyQueue.put(event.key)
            pygame.display.update()
        stonetile = pygame.image.load("stone_tile.png").convert()
        size = (64, 64)
        stonetile = pygame.transform.scale(stonetile, size)
        for wall in levelStructure.walls:
            canvas.blit(stonetile, (( wall.x * 64), (wall.y * 64)))
    LogicThread.join()
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
