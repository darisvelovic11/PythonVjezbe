class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __eq__(self, other):
        return  self.title == other.title and self.author==other.author
    
    def __lt__(self,other):
        return self.pages<other.pages
    
b1 = Book("Dune", "Frank Herbert", 412)
b2 = Book("1984", "George Orwell", 328)
b3 = Book("Dune", "Frank Herbert", 412)

print(b1)
print(repr(b1))
print(b1 == b3)     # True
print(b1 == b2)     # False
print(b2 < b1)      # True  (328 < 412)
