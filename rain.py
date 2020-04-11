from vpython import *
from random import randint

class Cloud:
    def __init__(self, pos, drops, lightning):
        self.lightning = lightning
        self.drops = drops
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.shape = None
        self._define_shape()

    def _define_shape(self):
        self.shape = [
            sphere(pos=vector(self.x, 4+self.y, self.z), radius=.5),
            sphere(pos=vector(-0.5+self.x, 3.8+self.y, self.z), radius=.5),
            sphere(pos=vector(.5+self.x, 3.8+self.y, self.z), radius=.5),
        ]
        for i in range(len(self.drops)):
            random_pos = randint(0, 2)
            self.drops[i].setpos(vector(self.shape[random_pos].pos))


    def to_rain(self):
        drop_down = randint(0, 9)
        
        x, y, z = self.drops[drop_down].getpos()

        if y <= 0:
            y = 3.8+self.y
            x = self.x

        self.drops[drop_down].setpos(vector(x+(drop_down/100), y-0.2, z))

        show_lightning = randint(1, 10000)
        if show_lightning == 10000:
            self.lightning.show()
            for i in range(100000): pass
            self.lightning.hide()
        
        
class Drop:
    def __init__(self):
        self.shape = sphere(color=vector(135/255,206/255,250/255), radius=.1)

    def setpos(self, position):
        self.shape.pos = position

    def getpos(self):
        x = self.shape.pos.x
        y = self.shape.pos.y
        z = self.shape.pos.z

        return (x, y, z)


class Lightning:
    def __init__(self, position):
        self.x, self.y, self.z = position
        self.shape = [
            cylinder(
                pos=vector(0+self.x, 0+self.y, 0+self.z), 
                radius=0.1,
                axis=vector(1, 2, 0),
                color=color.black
            ),
        
            cylinder(
                pos=vector(1+self.x, 2+self.y, 0+self.z), 
                radius=0.1,
                axis=vector(-1, 0, 0),
                color=color.black
            ),
            
            cylinder(
                pos=vector(0+self.x, 2+self.y, 0+self.z), 
                radius=0.1,
                axis=vector(1, 2, 0),
                color=color.black
            ),
        ]

    def show(self):
        self.shape[0].color = color.yellow
        self.shape[1].color = color.yellow
        self.shape[2].color = color.yellow
        return 

    def hide(self):
        self.shape[0].color = color.black
        self.shape[1].color = color.black
        self.shape[2].color = color.black
        return 
        
        


if __name__ == '__main__':
    try:
        drops1 = []
        drops2 = []
        drops3 = []
        drops4 = []
        lightning1= Lightning((-2.5,0,0))
        lightning2= Lightning((-1,0,0))
        lightning3= Lightning((1,0,0))
        lightning4= Lightning((2.5,0,0))
        
        for i in range(10):
            drops1.append(Drop())
            drops2.append(Drop())
            drops3.append(Drop())
            drops4.append(Drop())
        
        cloud1 = Cloud((-2.5,0,0), drops1, lightning1)
        cloud2 = Cloud((-1,0,0), drops2, lightning2)
        cloud3 = Cloud((1,0,0), drops3, lightning3)
        cloud4 = Cloud((2.5,0,0), drops4, lightning4)

        while True:
            cloud1.to_rain()
            cloud2.to_rain()
            cloud3.to_rain()
            cloud4.to_rain()
            
    except:
        pass
