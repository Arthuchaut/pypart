import pytest
from pypart.messenger import Email, Credentials, EmailFormatError


class TestCredentials:
    @pytest.mark.parametrize(
        'email, password, exception',
        [
            (Email('username@domain.com'), '123456', None),
            ('username@domain.com', '123456', None),
            (Email('username@domain.com'), None, ValueError),
            (None, '123456', ValueError),
            (None, None, ValueError),
        ],
    )
    def test___init__(
        self,
        email: Email | str,
        password: str,
        exception: Exception | None,
    ) -> None:
        if exception:
            with pytest.raises(exception):
                creds: Credentials = Credentials(email, password)
        else:
            creds: Credentials = Credentials(email, password)

            assert isinstance(creds.email, Email)
            assert isinstance(creds.password, str)
            assert str(creds.email) == str(email)
            assert creds.password == password
