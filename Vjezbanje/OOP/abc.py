class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"{self.name} has {len(self.books)} books"
    
    def __contains__(self, book):
        return book in self.books
    
    def __getitem__ (self,index):
        return self.books[index]

lib = Library("City Library")
lib.add_book("Dune")
lib.add_book("1984")
lib.add_book("The Hobbit") 

print(len(lib))
print(lib)
print("Dune" in lib)
print("Harry Potter" in lib)
print(lib[0])
