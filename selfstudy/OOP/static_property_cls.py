# _attribute - protected attribute for use inside class
# __attribute - private attribute for use inside class
# @classmethod - decorator for classmethod. Instead of 'self' get 'cls'
# as first argument independent of usage with class or instance.


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password  # setter called to set __password

    @property                   # password made property
    def password(self):
        return self.__password

    @staticmethod               # static method (without "self")
    def is_alphanum(passwd: str):
        if passwd.isalpha() or passwd.isnumeric():
            return False
        return True

    @password.setter            # property "password" setter function
    def password(self, passwd):
        if not isinstance(passwd, str):
            raise TypeError("Please enter string")
        if len(passwd) < 5:
            raise ValueError("Password should be 5+ chars")
        # staticmethod is called with class prefix
        if not User.is_alphanum(passwd):
            raise ValueError("Password should be alphanum")
        self.__password = passwd


q = User("Ivan", "dsdsd2fs")
q.password = "123456a"
print(q.password)
