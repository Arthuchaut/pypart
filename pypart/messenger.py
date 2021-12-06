import re


class Email:
    '''The email class.
    Allow to check email format validity and offer some
    practicals tools.

    Attributes:
        domain (str): The email domain name.
        username (str): The email username.
    '''

    def __init__(self, email: str) -> None:
        '''The constructor.'''

        self._email = self._validator(email)

    @property
    def domain(self) -> str:
        '''Returns the domain name from the email.

        Returns:
            str: The domain name.
        '''

        return self._email.split('@')[-1]

    @property
    def username(self) -> str:
        '''Returns the username from the email.

        Returns:
            str: The username.
        '''

        return self._email.split('@')[0]

    def _validator(self, email: str) -> str:
        '''Check the email format validity.

        Args:
            email (str): The email address to control.

        Raises:
            EmailFormatError: If the format does not match the expected one.

        Returns:
            str: The email address.
        '''

        if not re.match(r'^(\w|-|\.)+@\w{2,}\.\w{2,10}$', email):
            raise EmailFormatError(f'{email} is not a valid email.')

        return email

    def __str__(self) -> str:
        '''Returns the email address when called str() function.'''

        return self._email


class EmailFormatError(Exception):
    ...
