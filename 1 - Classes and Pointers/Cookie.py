class Cookie:
    def __init__(self, colour):
        self.colour = colour

    def getColour(self):
        return self.colour
    
    def setColour(self, colour):
        self.colour = colour

cookie_one = Cookie('blue')
cookie_two = Cookie('pink')

print('Cookie one is', cookie_one.getColour())
print('Cookie two is', cookie_two.getColour())

cookie_one.setColour('black')

print('Cookie one is now', cookie_one.getColour())
print('Cookie two is still', cookie_two.getColour())