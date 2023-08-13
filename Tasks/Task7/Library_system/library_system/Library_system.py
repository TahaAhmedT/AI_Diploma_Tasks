
class LibrarySystem:
    def log_in(self):
        email = input(print("plz enter your email: "))
        password = input(print("plz enter your password: "))
        verify = Validation.Validation()
        if not verify.verify_email(email) or not verify.verify_password(password):
            print("sorry sir, the password or email is wrong, try again!")
            return 0
        print("successful login!")

    def register(self):
        user_type = int(input(print("do you want to register as:\n1. Client\n2. Librarian\n3. Admin")))
        name = input(print("plz enter your name: "))

        validate = Validation.Validation()

        phone_number = input(print("plz enter your phone number: "))
        while not validate.validate_phone_number(phone_number):
            phone_number = input(print("this phone number is not valid, please enter a valid one: "))

        email = input(print("plz enter your email: "))
        while not validate.validate_email(email):
            email = input(print("this email is not valid, please enter a valid one: "))

        age = input(print("plz enter your age: "))
        address = input(print("plz enter your address: "))

        password = input(print("plz enter your password: "))
        while not validate.validate_password(password):
            password = input(print("this password is not valid, please enter a valid one: "))

        if user_type == 1:
            credit_card = input(print("plz enter your credit card: "))
            new_client = User.Client(name, phone_number, email, age, address, password, user_type, credit_card)
            Database.list_of_users.append(new_client)

        elif user_type == 2:
            new_librarian = User.Librarian(name, phone_number, email, age, address, password, user_type)
            Database.list_of_users.append(new_librarian)

        elif user_type == 3:
            new_admin = User.Admin(name, phone_number, email, age, address, password, user_type)
            Database.list_of_users.append(new_admin)

        print("register successfully!")
