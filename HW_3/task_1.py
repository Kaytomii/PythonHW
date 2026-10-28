class Book:
    def __init__(self, title, author, year, pages):
        if pages <= 0:
            raise ValueError("Page count must be positive")
        if year <= 0:
            raise ValueError("Publication year must be positive")

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}, {self.pages} pages"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.year}, {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages + other.pages

    def __contains__(self, word):
        return word.lower() in self.title.lower()

    def __bool__(self):
        return self.pages > 0

b = Book("Name", "Test", 1997, 350)
print(b)