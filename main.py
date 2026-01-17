import pygame
from pygame.locals import *
from threading import Thread
import time
import queue
import sys
import json

running = True
keyQueue = queue.Queue()
gameState = queue.Queue()

class ActionHandler:
    def __init__(self):
        self.keyMap = {
        }
    def readConfig(self):
        with open("keyconfig.json", "r") as f:
            config = json.load(f)
        for methodName, keyName in config.items():
            method = getattr(self, methodName, None)
            if not callable(method):
                raise ValueError(f"Unknown config action '{method_name}' in config, please reset")
            #this maps the config key to the method
            try:
                keyValue = getattr(pygame, keyName)
            except AttributeError:
                raise ValueError(f"Unknown config action '{method_name}' in config, please reset")
            self.keyMap[keyValue] = method
    def attack(self):
        print("attack")
    def left(self):
        print("left")
    def right(self):
        print("right")
    def execute(self, key):
        try:
            self.keyMap[key]()
        except KeyError:
            print(f"unkown key '{key}'")

class Logic(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        global running
        actionHandler = ActionHandler()
        actionHandler.readConfig()
        while running:
            while not keyQueue.empty():
                actionHandler.execute(keyQueue.get())
            print("hej")
            time.sleep(1)

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
        imp = pygame.image.load("stone_tile.png").convert()
        canvas.blit(imp, (0, 0))
    LogicThread.join()
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
