import json
import pygame
from pygame.locals import *

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
    def up(self):
        print("up")
    def down(self):
        print("down")
    def execute(self, key):
        try:
            self.keyMap[key]()
        except KeyError:
            print(f"unkown key '{key}'")
