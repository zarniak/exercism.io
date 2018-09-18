class SpaceAge(object):
    def __init__(self, seconds):
        print('Earth = ' + '{0:.2f}'.format(seconds/60/60/24/365) + ' years old')
        print('Mercury = ' + '{0:.2f}'.format(seconds/60/60/24/365*0.2408467) + ' years old')
#why i get rounded integer not float/double figure for Earth

print SpaceAge(71997456)
#why i get message <__main__.SpaceAge object at 0x7f180bcd9610>


#Earth: orbital period 365.25 Earth days, or 31557600 seconds
#Mercury: orbital period 0.2408467 Earth years
#Venus: orbital period 0.61519726 Earth years
#Mars: orbital period 1.8808158 Earth years
#Jupiter: orbital period 11.862615 Earth years
#Saturn: orbital period 29.447498 Earth years
#Uranus: orbital period 84.016846 Earth years
#Neptune: orbital period 164.79132 Earth years

#abstract from stackoverflow
#class A(object):
#    def __init__(self):
#        self.x = 'Hello'
#
#    def method_a(self, foo):
#        print self.x + ' ' + foo
#
#a = A()               # We do not pass any argument to the __init__ method
#a.method_a('Sailor!') # We only pass a single argument
