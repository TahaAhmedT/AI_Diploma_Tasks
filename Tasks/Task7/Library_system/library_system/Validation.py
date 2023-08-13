

class Validation:
    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def validate_password(self, password):
        # Password must be at least 8 characters long
        if len(password) < 8:
            return False

        # Password must contain at least one uppercase letter, one lowercase letter, and one digit
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False

        # Password is valid
        return True

    def validate_phone_number(self, phone_number):
        # Phone number must start with the country code '+20' or '0020'
        if phone_number.startswith('+20') or phone_number.startswith('0020'):
            # Remove the country code from the phone number
            phone_number = phone_number[3:]

            # Phone number must be 11 digits long after removing the country code
            if len(phone_number) == 11 and phone_number.isdigit():
                # Phone number is valid
                return True

        # Phone number is not valid
        return False

    def verify_email(self, email):
        for i in list_of_users:
            if email == i.email:
                return True
        return False

    def verify_password(self, password):
        for i in list_of_users:
            if password == i.password:
                return True
        return False
