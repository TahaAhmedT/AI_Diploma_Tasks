import Book
from Database import list_of_books, list_of_users


class User:
    ID = 0

    def __init__(self, name, phone_number, email, age, address, password, user_type):
        self.id = User.ID + 1
        User.ID += 1
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.age = age
        self.address = address
        self.password = password
        self.user_type = user_type
    
    def inquery_book(self):
        for book in list_of_books:
            print("Book ID: ", book.id)
            print("Book name: ", book.name)
            print("Book Category: ", book.category)
            print("#paper: ", book.no_paper)
            print("Author: ", book.author)
            print("Publisher: ", book.publisher)
            print("Year of publication: ", book.year_of_pub)
            print("Book Price: ", book.price)
            print("\n")


class Client(User):
    def __init__(self, name, phone_number, email, age, address, password, user_type, credit_card):
        super().__init__(name, phone_number, email, age, address, password, user_type)
        self.credit_card = credit_card
        self.no_returned = 0
        self.no_borrowed = 0
        self.no_reserved = 0

    def purchase_book(self):
        self.inquery_book()
        answer = 1
        total_price = 0
        purchased_books = []
        while answer == 1:
            book_id = input(print("plz enter the book id: "))
            for book in list_of_books:
                if book_id == book.id:
                    print("the price of the book is: ", book.price)
                    total_price += book.price
                    purchased_books.append(book)

            answer = int(input(print("do you want to purchase another book?(1. YES or 2. NO): ")))

        answer = input(print("do you want to checkout or cancel (1. checkout or 2. cancel): "))
        if answer == 1:
            self.purchasing_checkout(total_price, purchased_books)
        else:
            print("You are welcome at any time!")

    def purchasing_checkout(self, total_price, purchased_books):
        if self.credit_card >= total_price:
            print("your item/s: ")
            for book in purchased_books:
                print("book name: ", book.name)
                print("book price: ", book.price)
                self.no_reserved += 1
            print("total price is: ", total_price)

        elif self.credit_card < total_price:
            print("sorry, you don't have enough money!")

    def borrow_book(self):
        self.inquery_book()
        book_id = int(input(print("please enter the book id: ")))

        for book in list_of_books:
            if book_id == book.id:
                print("book name: ", book.name)
                print("borrowing price: ", book.price * 0.15)
                book.show_due_date()

                answer = int(input(print("do you want to checkout or cancel (1. checkout or 2. cancel): ")))
                if answer == 1:
                    self.borrowing_checkout(book.price * 0.15)
                else:
                    print("you are welcome at any time!")

    def borrowing_checkout(self, price):
        if self.credit_card >= price:
            print("congrats!")
            print("please return the book on the due date.")
            self.no_borrowed += 1

        elif self.credit_card < price:
            print("sorry, you don't have enough money!")


class Librarian(User):
    def __init__(self, name, phone_number, email, age, address, password, user_type):
        super().__init__(name, phone_number, email, age, address, password, user_type)

    def add_book(self):
        name = input(print("plz enter the name of the book: "))
        publisher = input(print("plz enter the name of the Publisher: "))
        no_paper = input(print("plz enter the number of papers: "))
        price = input(print("plz enter the price: "))
        category = input(print("plz enter the category: "))
        author = input(print("plz enter the name of the author: "))
        has_parts = input(print("is this book has parts(YES or NO): "))
        if has_parts == "NO":
            has_parts = False
        else:
            has_parts = True

        year_of_pub = input(print("plz enter the Year of publication: "))
        no_available = input(print("plz enter the number of available pieces: "))
        due_date = input(print("plz enter the due date: "))
        new_book = Book.Book(name, publisher, no_paper, price, category, author, has_parts, year_of_pub, no_available, due_date)
        list_of_books.append(new_book)

    def delete_book(self):
        book_id = input(print("plz enter the id of the book: "))
        for book in list_of_books:
            if book_id == book.id:
                list_of_books.remove(book)
                print("Book deleted Successfully!")
                return 0
        print("this book is not in our database!")

    def update_book(self):
        book_id = input(print("plz enter the id of the book: "))
        for book in list_of_books:
            if book_id == book.id:
                book.no_paper = input(print("plz enter the number of papers: "))
                book.price = input(print("plz enter the prise: "))
                book.no_available = int(input(print("plz enter the number of available pieces: ")))
                book.due_date = input(print("plz enter the due date: "))
                print("the book is updated successfully!")
                return 0
        print("this book is not in our databased!")


class Admin(User):
    def __init__(self, name, phone_number, email, age, address, password, user_type):
        super().__init__(name, phone_number, email, age, address, password, user_type)

    def add_user(self):
        name = input(print("plz enter the name of the user: "))
        phone_number = input(print("plz enter the phone number of the user: "))
        email = input(print("plz enter the email of the user: "))
        age = int(input(print("plz enter the age of the user: ")))
        address = input(print("plz enter the address of the user: "))
        password = input(print("plz enter the password of the user: "))
        user_type = input(print("is this user a Client or not(YES or NO): "))

        if user_type == "YES":
            credit_card = input(print("plz enter the credit card of the client: "))
            new_client = Client(name, phone_number, email, age, address, password, 1, credit_card)
            list_of_users.append(new_client)
            print("The new client is added successfully!")
            return 0

        else:
            new_librarian = Librarian(name, phone_number, email, age, address, password, 2)
            list_of_users.append(new_librarian)
            print("The new librarian is added successfully!")
            return 0

    def delete_user(self):
        user_id = input(print("plz enter the id of the user: "))
        for user in list_of_users:
            if user_id == user.id:
                list_of_users.remove(user)
                print("this user is deleted successfully!")
                return 0

        print("this user is not in our database!")

    def update_user(self):
        user_id = input(print("plz enter the id of the user: "))
        for user in list_of_users:
            if user_id == user.id:
                user.phone_number = input(print("plz enter the phone number: "))
                user.email = input(print("plz enter the email: "))
                user.address = input(print("plz enter the address: "))
                user.password = input(print("plz enter the password: "))
                user_type = input(print("is this user a client(YES or NO): "))
                if user_type == "YES":
                    user.credit_card = input(print("plz enter the credit card: "))
                    print("user is updated successfully!")
                    return 0
                else:
                    print("user is updated successfully!")

    def search_user(self):
        user_id = input(print("plz enter the id of the user: "))
        for user in list_of_users:
            if user_id == user.id:
                print("user name: ", user.name)
                print("user age: ", user.age)
                print("user address: ", user.address)
                print("user email: ", user.email)
                return 0

        print("this user is not found!")
