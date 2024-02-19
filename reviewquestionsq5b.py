class library_member:
    def __init__(self, member_id, name, borrowed_books, lib_name, located):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books
        self.lib_name = lib_name
        self.located = located
        print(member_id, name, borrowed_books)
    def common(self):
        print(f"Welcome to the library. My name is {self.lib_name}")
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(self.borrowed_books)
    def display_information(self):
        print(self.member_id)
        print(self.name)
        print(self.borrowed_books)
class librarian(library_member):
    def name_librarian(self):
        print(f"Welcome {self.lib_name}. You ID number is {self.member_id}. Your list of borrowed books is {self.borrowed_books}")
        
class structures(library_member):
    def tables(self, color):
        self.color = color
        print(f"Hi {self.lib_name}. The table is located {self.located} the walls of the library. Your Member ID number is {self.member_id} .")
    def chairs(self, number):
        self.number = number
        print(f"Hello {self.name}. welcome to the library. My name is {self.lib_name}. We have {self.number} {self.color} chairs.")
    
class shelves(library_member):
    def shelve(self, form, no_of_shelves):
        self.form = form
        self.no_of_shelves = no_of_shelves
        print(f"Hello {self.name}. We have {self.no_of_shelves} shelves. They are arranged {self.form}")
libr = library_member(120, "Kim", ["tr1", "tr2", "tr3", "tr5", "tr4"], "Kimani", "alongside")
libr.borrow_book(book = input("Enter the book you borrowed : "))
libr.display_information()
libr.common()
lib = librarian(100, "Kimutai", ["tr1", "tr2", "tr3", "tr5", "tr4"], "Jackson", "alongside")
lib.name_librarian()
st = structures(1200, "Wycliff", ["tr1", "tr2", "tr3", "tr5", "tr4"], "Alfred", "alongside")
st.tables("brown")
st.chairs(20000)
sh = shelves(12000, "Fredrick", ["tr1", "tr2", "tr3", "tr5", "tr4"], "Jacob", "alongside")
sh.shelve("alphabetically", 600)