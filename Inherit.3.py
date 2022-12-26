class SpaceObject:

    def __init__(self, size):
        self.size = size


class Star(SpaceObject):

    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness


    def shine(self):
        print(f"Яркость звезды: {self.brightness}")

    def size(self):
        print(f"Размер звезды: {self.size}")


class Planet(SpaceObject):
    def __init__(self, size, population, growth):
        super().__init__(size)
        self.population = population
        self.growth = growth


    def population_in_years(self, years):
        print(f"Через {years} лет численность населения составит:{self.population + self.growth * years} ")

star = Star(100, 98)
star.shine()


planet = Planet(300, 1000, 100)
planet.population_in_years(10)

