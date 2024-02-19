class library_book:
    def __init__(self, title, author, publication_year, borrowed):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = borrowed
        
    def borrow_book(self):
        print(f"Is the book borrowed ? : {self.borrowed}")
        
    def return_book(self, return_date):
        print(f"The book was returned on : {return_date} ")
        print(f"Is the book returned to the library: : {self.borrowed}")
    
    def display_information(self):
        print(self.title)
        print(self.author)
        print(self.publication_year)
        print(self.borrowed)
lib = library_book("Dark Of Night", "Kim Jackson", 2023, False)
lib.borrow_book()
lib.return_book("22nd May, 2023")
lib.display_information()