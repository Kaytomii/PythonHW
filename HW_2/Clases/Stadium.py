class Stadium:

    def __init__(self, Name="unknown", OpeningDate="unknown",
                 Country="unknown", City="unknown", Capacity="unknown"):
        self.__Name = Name
        self.__OpeningDate = OpeningDate
        self.__Country = Country
        self.__City = City
        self.__Capacity = Capacity

    def FillStadiumFields(self):
        self.__Name = input("Enter stadium name: ")
        self.__OpeningDate = input("Enter opening date: ")
        self.__Country = input("Enter country: ")
        self.__City = input("Enter city: ")
        self.__Capacity = input("Enter capacity: ")

    def __str__(self):
        return (f"Stadium Name: {self.__Name}, Opening Date: {self.__OpeningDate}, "
                f"Country: {self.__Country}, City: {self.__City}, Capacity: {self.__Capacity}")


stadium = Stadium()
stadium.FillStadiumFields()
print(stadium)