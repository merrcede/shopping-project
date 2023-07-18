import re
from getpass import getpass


class ValidationError(ValueError):
    pass


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def sign_up(self, username: str, password: str, date_of_brith: str) -> None:
        """
        Register a new user on the site.

        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            date_of_birth (str): The date of birth for the new user.

        Returns:
            None

        Raises:
            ValidationError: If the username, password, or date of birth is invalid.
            :param username:
            :param password:
            :param date_of_brith:
            """
        self.username = username
        self.password = password
        self.date_of_brith = date_of_birth

    def login(self, username: str, password: str) -> bool:
        """
        Login with the provided credentials.

        Args:
            username (str): The username for login.
            password (str): The password for login.

        Returns:
            bool: True if the login is successful.

        Raises:
            Exception: If the credentials are incorrect.
        """
        if not self.username == username and self.password == password:
            raise Exception('The username or password is wrong.')
        else:
            return True

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[A-Za-z\d@#$%^&+=]{8,}$', value):
            raise ValidationError("Invalid password!")
        self.__password = value

    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.username}>'


if __name__ == '__main__':
    print("Welcome")
    print("Register: ")

    while True:
        username = input("Username: ")
        password = getpass("Password: ")
        date_of_birth = input("Date of Birth: ")
        print('Enter your birthday to be surprised on your birthday ;)')
        try:
            user = User(None, None)
            user.sign_up(username, password, date_of_birth)
            print("You are registered successfully!")
            break
        except ValidationError as e:
            print(e)

    while True:
        print("Login")
        username = input("Username: ")
        password = getpass("Password: ")

        try:
            user.login(username, password)
            print("You are logged in!")
            break
        except Exception as e:
            print(e)
