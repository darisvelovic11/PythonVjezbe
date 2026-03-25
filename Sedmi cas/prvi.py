class Post:
    def __init__(self, id, name, description, author="Admin"):
        # self = {}
        self.name = name
        self.id = id
        self.description = description
        self.author = author
        # return self

post1 = Post(1, "Rezultati iz Pythona", "Deskripcija", 'Marko Marovic')