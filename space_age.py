SECONDS_IN_EARTH_YEAR = 60 * 60 * 24 * 365
PLANETS_EARTH_YEAR_LENGTH = {
    'Earth': 1,
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132,
}

class SpaceAge(object):

    def __init__(self, seconds):
        self.seconds = seconds
        years = self.seconds / SECONDS_IN_EARTH_YEAR
        self.planets_age = {k: years * v for (k, v) in PLANETS_EARTH_YEAR_LENGTH.items()}

    def on_mercury(self):
       return self.planets_age['Mercury']

    def on_venus(self):
        return self.planets_age['Venus']

    def on_earth(self):
        return self.planets_age['Earth']

    def on_mars(self):
        return self.planets_age['Mars']

    def on_jupiter(self):
        return self.planets_age['Jupiter']

    def on_saturn(self):
        return self.planets_age['Saturn']

    def on_uranus(self):
        return self.planets_age['Uranus']

    def on_neptune(self):
        return self.planets_age['Neptune']

SpaceAge.on_neptune(71997456)
