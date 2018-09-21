class SpaceAge(object):
    def __init__(self, seconds):
        planets = [
            ['Earth', 1], ['Mercury', 0.2408467], ['Venus', 0.61519726],
            ['Mars', 1.8808158], ['Jupiter', 11.862615], ['Saturn', 29.447498],
            ['Uranus', 84.016846], ['Neptune', 164.79132]]
        for planet in planets:
            print('{} = {0:.2f} years old'.format(planet[0], seconds/60/60/24/365*planet[1]))

SpaceAge(71997456)
