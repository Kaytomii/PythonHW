class Car:

    def __init__(self, Model="unknown", Year="unknown", Manufacturer="unknown",
                 EngineVolume="unknown", Color="unknown", Price="unknown"):
        self.__Model = Model
        self.__Year = Year
        self.__Manufacturer = Manufacturer
        self.__EngineVolume = EngineVolume
        self.__Color = Color
        self.__Price = Price

    def FillCarFields(self):
        self.__Model = input("Enter car model: ")
        self.__Year = input("Enter year of production: ")
        self.__Manufacturer = input("Enter manufacturer: ")
        self.__EngineVolume = input("Enter engine volume: ")
        self.__Color = input("Enter car color: ")
        self.__Price = input("Enter price: ")

    def __str__(self):
        return (f"Model: {self.__Model}, Year: {self.__Year}, Manufacturer: {self.__Manufacturer}, "
                f"Engine Volume: {self.__EngineVolume}, Color: {self.__Color}, Price: {self.__Price}")


car = Car()
car.FillCarFields()
print(car)