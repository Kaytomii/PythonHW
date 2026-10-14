class Person:
    __counter = 0

    def __init__(self, NameandSurname = "unknown", DateofBirth = "unknown", Adress = "unknown",
                 ContactNumber = "unknown", Country = "unknown", City = "unknown", Age = 18):
        Person.__counter += 1
        self.__NameandSurname = NameandSurname
        self.__DateofBirth = DateofBirth
        self.__Adress = Adress
        self.__ContactNumber = ContactNumber
        self.__Country = Country
        self.__City = City
        self.__Age = Age

    def FillPersonField(self):
        self.__NameandSurname = input("Enter your name and surname: ")
        self.__DateofBirth = input("Enter your date of birth: ")
        self.__Adress = input("Enter your adress: ")
        self.__ContactNumber = input("Enter your contact number: ")
        self.__Country = input("Enter your country: ")
        self.__City = input("Enter your city: ")
        self.__Age = int(input("Enter your age: "))

    def __str__(self):
        return f"Name and Surname: {self.__NameandSurname}, Date of Birth: {self.__DateofBirth}" \
               f", Adress: {self.__Adress}, Conctact number: {self.__ContactNumber}, Country: {self.__Country}" \
               f", City: {self.__City}, Age: {self.__Age}"
    @property
    def NameandSurname(self):
        return self.__NameandSurname

    @NameandSurname.setter
    def NameandSurname(self, NewNameandSurname):
        if NewNameandSurname == "":
            raise ValueError("Name and Surname is null")

        self.__NameandSurname = NewNameandSurname

    @staticmethod
    def get_counter():
        return Person.__counter

person = Person()
person.FillPersonField()
print(person)