class library_member:
    def __init__(self, member_id, name, borrowed_books):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books
        print(member_id, name, borrowed_books)
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(self.borrowed_books)
    def display_information(self):
        print(self.member_id)
        print(self.name)
        print(self.borrowed_books)
libr = library_member(120, "Kim", ["tr1", "tr2", "tr3", "tr5", "tr4"])
libr.borrow_book(book = input("Enter the book you borrowed : "))
libr.display_information()
