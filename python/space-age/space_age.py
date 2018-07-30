class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return self.format_number(self.seconds / 31557600)

    def on_earth_original(self):
        return self.seconds / 31557600

    def on_mercury(self):
        return self.format_number(self.on_earth_original() / 0.2408467)

    def on_venus(self):
        return self.format_number(self.on_earth_original() / 0.61519726)

    def on_mars(self):
        return self.format_number(self.on_earth_original() / 1.8808158)

    def on_jupiter(self):
        return self.format_number(self.on_earth_original() / 11.862615)

    def on_saturn(self):
        return self.format_number(self.on_earth_original() / 29.447498)

    def on_uranus(self):
        return self.format_number(self.on_earth_original() / 84.016846)

    def on_neptune(self):
        return self.format_number(self.on_earth_original() / 164.79132)

    def seconds(self):
        return self.seconds

    def format_number(self, number):
        return round(number, 2)
