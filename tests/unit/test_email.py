import pytest
from pypart.messenger import Email, EmailFormatError


class TestEmail:
    @pytest.mark.parametrize(
        'email, exception',
        [
            ('username@domain.com', None),
            ('user.name@domain.com', None),
            ('user-name@domain.com', None),
            ('user_name@domain.com', None),
            ('@domain.com', EmailFormatError),
            ('username@', EmailFormatError),
            ('username', EmailFormatError),
            ('username@domain.f', EmailFormatError),
            ('username@domain', EmailFormatError),
            ('username@domain.verylongtopleveldomainname', EmailFormatError),
            ('username@domain.co-m', EmailFormatError),
            ('user!name@domain.co-m', EmailFormatError),
        ],
    )
    def test_validator(
        self, email: str, exception: EmailFormatError | None
    ) -> None:
        if exception:
            with pytest.raises(exception):
                Email(email)
        else:
            Email(email)

    def test_domain(self) -> None:
        email: Email = Email('username@domain.com')
        assert email.domain == 'domain.com'

    def test_username(self) -> None:
        email: Email = Email('username@domain.com')
        assert email.username == 'username'

    def test___str__(self) -> None:
        email: Email = Email('username@domain.com')
        assert str(email) == 'username@domain.com'
