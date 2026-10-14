class Book:

    def __init__(self, Title="unknown", Year="unknown", Publisher="unknown",
                 Genre="unknown", Author="unknown", Price="unknown"):
        self.__Title = Title
        self.__Year = Year
        self.__Publisher = Publisher
        self.__Genre = Genre
        self.__Author = Author
        self.__Price = Price

    def FillBookFields(self):
        self.__Title = input("Enter book title: ")
        self.__Year = input("Enter year of publication: ")
        self.__Publisher = input("Enter publisher: ")
        self.__Genre = input("Enter genre: ")
        self.__Author = input("Enter author: ")
        self.__Price = input("Enter price: ")

    def __str__(self):
        return (f"Title: {self.__Title}, Year: {self.__Year}, Publisher: {self.__Publisher}, "
                f"Genre: {self.__Genre}, Author: {self.__Author}, Price: {self.__Price}")


book = Book()
book.FillBookFields()
print(book)