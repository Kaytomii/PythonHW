class Ship:
    def __init__(self, name, crew):
        self.name = name
        self.crew = crew

    def info(self):
        return f"Ship: {self.name}, Crew: {self.crew}"


class Frigate(Ship):
    def __init__(self, name, crew, missiles):
        super().__init__(name, crew)
        self.missiles = missiles

    def attack(self):
        return f"{self.name} launches {self.missiles} missiles"


class Destroyer(Ship):
    def __init__(self, name, crew, cannons):
        super().__init__(name, crew)
        self.cannons = cannons

    def fire(self):
        return f"{self.name} fires {self.cannons} cannons"


class Cruiser(Ship):
    def __init__(self, name, crew, armor):
        super().__init__(name, crew)
        self.armor = armor

    def defend(self):
        return f"{self.name} activates armor level {self.armor}"

ship = Destroyer("Test", 120, 8)
print(ship.fire())