# program to create a system to manage a library
class library_book:

    def __init__(self, title, author, publication_year):

        self.title = title

        self.author = author

        self.publication_year = publication_year
    def display_info(self):

        print("Title:", self.title)

        print("Author:", self.author)

        print("Publication Year:", self.publication_year)
class FictionBook(library_book):

    def __init__(self, title, author, publication_year, genre):

        super().__init__(title, author, publication_year)

        self.genre = genre
    def display_info(self):

        super().display_info()

        print("Genre:", self.genre)
class NonFictionBook(library_book):

    def __init__(self, title, author, publication_year, topic):

        super().__init__(title, author, publication_year)

        self.topic = topic
    def display_info(self):

        super().display_info()

        print("Topic:", self.topic)
fiction_book = FictionBook("Gone Too Far", "Suzanne Brockmann", 2003, "Military Romance")
non_fiction_book = NonFictionBook("For The Record", "Aden Duale", 2023, "Political")
fiction_book.display_info()
print()
def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
class FictionBook(library_book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre
    def display_info(self):
        super().display_info()
        print("Genre:", self.genre)
class NonFictionBook(library_book):
    def __init__(self, title, author, publication_year, topic):
        super().__init__(title, author, publication_year)
        self.topic = topic
    def display_info(self):
        super().display_info()
        print("Topic:", self.topic)
fiction_book = FictionBook("Gone Too Far", "Suzanne Brockmann", 2003, "Military Romance")
non_fiction_book = NonFictionBook("For The Record", "Aden Duale", 2023, "Political")
print()
fiction_book.display_info()
print()
non_fiction_book.display_info()
print()
non_fiction_book.display_info()
print()
fiction_book.display_info()