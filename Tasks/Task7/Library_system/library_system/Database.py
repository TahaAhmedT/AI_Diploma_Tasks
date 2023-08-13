



class Database:
    def load_users_data(self):
        client1 = User.Client("taha", "011", "taha@gmail.com", 20, "giza", "12345", 1, "1000")
        client2 = User.Client("ahmed", "012", "ahmed@gmail.com", 22, "cairo", "6789", 1, "2000")
        list_of_users.append(client1)
        list_of_users.append(client2)

    def load_books_data(self):
        book1 = Book.Book("elhob", "aseer elhob", "230", 120, "romantic", "elasheq", False, "2020", 20, "after two weeks")
        book2 = Book.Book("first million", "aseer elkotob", "630", 320, "economic", "million", False, "2000", 3, "after one month")
        list_of_books.append(book1)
        list_of_books.append(book2)

