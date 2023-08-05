from abc import ABC

from PyGine import PyGinegame as Game, Component
from PyGine.Camera import Camera
from PyGine.Transform import Transform
class GameObject(ABC) :
    def __init__(self,name="",tags=["gameObjects"]):
        self.tags = tags
        self.name = name
        self.transform = Transform()
        self.Components = []
        self.destroy = False
        self.tracked = False
        self.Used = False
        self.started = False


    def start(self):
        """
        The start methode is called after the start of component
        @use : init the variables you need
        """
        pass

    def earlyStart(self):
        """
        The earlyStart methode is called before the start of the components
        @use : declare the component or init the variables you need
        """
        pass

    def Mstart(self):
        """
        Internal methode of PyGine, don't touch
        """
        if not self.started :
            self.earlyStart()
            for c in self.Components :
                c.Mstart()
            self.started = True
            self.Used = True
            self.start()

    def update(self,dt):
        pass

    def Mupdate(self,dt):

        if(self.destroy) :
            Game.get().CurrentScene.removeGameObject(self)
        else :
            for composant in self.Components:
                composant.Mupdate(dt)
                if(self.destroy) :
                    return


        if self.tracked :
            Camera.PX = Camera.DX+self.transform.position.x - Game.get().width/2
            Camera.PY = Camera.DY+self.transform.position.y - Game.get().height/2
        self.update(dt)

    def addComponent(self, composant):
        if self.Used :
            composant.Mstart()
        self.Components.append(composant)

    def AttachCamera(self,state):
        self.tracked = state

    def getComponent(self,class_) :
        for el in self.Components :
            if el.__class__.__name__ == class_ :
                return el
        return None

    def Mend(self):
        for c in self.Components :
            c.Mend()
        self.end()

    def end(self):
        pass

    def onCollision(self,o):
        for c in self.Components :
            c.onCollide(o)

    def onMouseClick(self,button):
        for c in self.Components :
            c.onMouseClick(button)
