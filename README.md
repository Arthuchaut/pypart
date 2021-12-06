# pypart

A simple CLI tool that associate pairs of peoples.

## Usage

```sh
python -m pypart --emitter-email=<emitter_email> --emitter-pass=<emitter_password> --receiver <receiver_email_1> --receiver <receiver_email_2> --receiver <receiver_email_3> --message="Hello {{receiver_email}},\n\nYou had choosen to be associated with {{associated_email}}!"
```


## Implementation

```py

class Email:
    def __init__(self, email: str) -> None:
        self._email: str = self._validator(email)

    @property
    def domain(self) -> str:
        return self._email.split('@')[-1]

    @property
    def username(self) -> str:
        return self._email.split('@')[0]

    def _validator(self, email: str) -> str:
        ...

    def __str__(self) -> str:
        return self._email

class EmailFormatError(Exception):
    ...

@dataclass
class _Credentials:
    email: Email
    password: str


class Messenger:
    _SMTP_CONFIG: ClassVar[dict[str, dict[str, Any]]] = [
        'gmail': {
            'server': 'smtp.gmail.com',
            'port': 456,
        }
    ]

    def __init__(self, emitter_credentials: _Credentials) -> None:
        ...

    def __enter__(self) -> Mailer:
        ...
        return self

    def __exit__(self, ...) -> None:
        ...

    def send(self, receiver: Email, subject: str, message: str) -> None:
        ...

    def _interpolate_message(self, message: str, receiver: Email) -> str:
        ...

class RandomCombiner:
    @classmethod
    def generate_pairs(cls, emails: list[Email]) -> list[tuple[Mail, Mail]]:
        ...