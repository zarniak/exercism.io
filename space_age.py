class SpaceAge(object):
    def __init__(self, seconds):
        print('Earth = ' + '{0:.2f}'.format(seconds/60/60/24/365) + ' years old')
        print('Mercury = ' + '{0:.2f}'.format(seconds/60/60/24/365*0.2408467) + ' years old')
        print('Venus = ' + '{0:.2f}'.format(seconds/60/60/24/365*0.61519726) + ' years old')
        print('Mars = ' + '{0:.2f}'.format(seconds/60/60/24/365*1.8808158) + ' years old')
        print('Jupiter = ' + '{0:.2f}'.format(seconds/60/60/24/365*11.862615) + ' years old')
        print('Saturn = ' + '{0:.2f}'.format(seconds/60/60/24/365*29.447498) + ' years old')
        print('Uranus = ' + '{0:.2f}'.format(seconds/60/60/24/365*84.016846) + ' years old')
        print('Mercury = ' + '{0:.2f}'.format(seconds/60/60/24/365*164.79132) + ' years old')

SpaceAge(71997456)
