class Publication:
    def __init__(self, name):
        self.name = name
    def print_information(self):
        print("Name:", self.name)


class Book (Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages
    def print_information(self):
        super().print_information()
        print ("Author:", self.author)
        print ("Pages:", self.pages)


class Magazine (Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        super().print_information()
        print ("Chief editor:", self.chief_editor)


duck_news = Magazine("Donald Tuck", "Aki Hyyppä")
train_book = Book("Compartment No. 6", "Rosa Liksom", 192)

duck_news.print_information()
print()
train_book.print_information()