from abc import ABC, abstractmethod

class Printer(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def print_doc(self):
        pass

class ExcellDocument(Printer):
    def __init__(self, model, title, text, ext, pages):
        super().__init__(model)
        self.title = title
        self.text = text
        self.ext = ext
        self.pages = pages

    def print_doc(self):
        print(f"[{self.model}] Excel printed: {self.title}, pages: {self.pages}")

class WordDocument(Printer):
    def __init__(self, model, title, text, ext, pages):
        super().__init__(model)
        self.title = title
        self.text = text
        self.ext = ext
        self.pages = pages

    def print_doc(self):
        print(f"[{self.model}] Word printed: {self.title}, pages: {self.pages}")

class HtmlDocument(Printer):
    def __init__(self, model, title, text, ext, pages):
        super().__init__(model)
        self.title = title
        self.text = text
        self.ext = ext
        self.pages = pages

    def print_doc(self):
        print(f"[{self.model}] HTML printed: {self.title}, pages: {self.pages}")

def print_doc(pr):
    if isinstance(pr, Printer):
        pr.print_doc()

print_doc(ExcellDocument("HP", "Test", "Some", "xls", 30))
print_doc(WordDocument("Canon", "Test", "Some", "docx", 40))
print_doc(HtmlDocument("Epson", "Test", "Some", "html", 10))
