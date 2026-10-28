class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


class CoffeeMachine(Device):
    def __init__(self, brand, model, pressure):
        super().__init__(brand, model)
        self.pressure = pressure

    def make_coffee(self):
        return f"{self.info()} is making coffee at {self.pressure} bar"


class Blender(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def blend(self):
        return f"{self.info()} is blending at {self.power} watts"


class MeatGrinder(Device):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def grind(self):
        return f"{self.info()} is grinding meat at speed {self.speed}"

cm = CoffeeMachine("Test", "Test model", 15)
print(cm.make_coffee())