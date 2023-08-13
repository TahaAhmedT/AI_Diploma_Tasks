class Book:
    ID = 0

    def __init__(self, name, publisher, no_paper, price, category, author, has_parts, year_of_pub, no_available, due_date):
        self.id = Book.ID + 1
        Book.ID += 1
        self.name = name
        self.publisher = publisher
        self.no_paper = no_paper
        self.price = price
        self.category = category
        self.author = author
        self.has_parts = has_parts
        self.year_of_pub = year_of_pub
        self.no_available = no_available
        self.due_date = due_date

    def show_due_date(self):
        print("The due date of ", self.name, " is ", self.due_date)
