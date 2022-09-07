import string


class Registration:
    def __init__(self, login, password):
        self.login, self.password = login, password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if Registration.is_correct_login(login):
            self.__login = login

    @staticmethod
    def is_correct_login(login):
        if login.find('@') == -1:
            raise ValueError("Login must include at least one ' @ '")
        if login.find('.') == -1:
            raise ValueError("Login must include at least one ' . '")
        return True

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if Registration.is_correct_password(password):
            self.__password = password

    @staticmethod
    def is_include_digit(password):
        for c in password:
            if c in string.digits:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        for c1 in password:
            if c1.isupper():
                for c2 in password:
                    if c2.islower():
                        return True
                return False
        return False

    @staticmethod
    def is_include_only_latin(password):
        for c in password:
            if c not in string.printable:
                return False
        return True

    @staticmethod
    def check_password_dictionary(password):
        with open('easy_passwords.txt', 'r') as input_file:
            for line in input_file:
                if password == line.rstrip():
                    return False
        return True

    @staticmethod
    def is_correct_password(password):
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if not 5 <= len(password) <= 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not Registration.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        return True