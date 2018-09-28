class SpaceAge(object):
    __init__(self, seconds):
        self.seconds = seconds
        self.planets = {
            'Earth': 1, 'Mercury': 0.2408467, 'Venus': 0.61519726,
            'Mars': 1.8808158, 'Jupiter': 11.862615, 'Saturn': 29.447498,
            'Uranus': 84.016846, 'Neptune': 164.79132
        }

    def on_mercury(self):
        return self.seconds/60/60/24/365*self.planets.get('Mercury')

    def on_venus(self):
        return self.seconds/60/60/24/365*self.planets.get('Venus')

    def on_earth(self):
        return self.seconds/60/60/24/365*self.planets.get('Earth')

    def on_mars(self):
        return self.seconds/60/60/24/365*self.planets.get('Mars')

    def on_jupiter(self):
        return self.seconds/60/60/24/365*self.planets.get('Jupiter')

    def on_saturn(self):
        return self.seconds/60/60/24/365*self.planets.get('Saturn')

    def on_uranus(self):
        return self.seconds/60/60/24/365*self.planets.get('Uranus')

    def on_neptune(self):
        return self.seconds/60/60/24/365*self.planets.get('Neptune')
SpaceAge(71997456)
