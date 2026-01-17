class GameObject:
    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture

class Structure(GameObject):
    def __init__(self, x, y, texture, collision):
        self.x = x
        self.y = y
        self.texture = texture
        self.collision = collision

class Entity(GameObject):
    def __init__(self, x, y, texture, collision, controllable):
        self.x = x
        self.y = y
        self.texture = texture
        self.collision = collision
        self.controllable = controllable
    def moveUp(self):
        self.y-=1
    def moveDown(self):
        self.y+=1
    def moveLeft(self):
        self.x-=1
    def moveRight(self):
        self.x+=1
