from typing import Any
import pytest
from pypart.type_checker import TypeChecker
from pypart.messenger import Email


class TestTypeChecker:
    @pytest.mark.parametrize(
        'value, type_, exception',
        [
            (
                [Email('username@domain.com'), Email('username2@domain.com')],
                list[Email],
                None,
            ),
            (
                [
                    ['hello', 'world'],
                    ['hello', 'world'],
                ],
                list[list[str]],
                None,
            ),
            (
                [
                    [
                        ['hello', 'world'],
                        ['whats', 'up'],
                    ],
                    [
                        ['hello', 'world'],
                        ['whats', 'up'],
                    ],
                ],
                list[list[list[str]]],
                None,
            ),
            (
                {
                    'hello': 2,
                    'whats': 4,
                },
                dict[str, int],
                None,
            ),
            (
                {
                    'hello': [1, 2, 4],
                    'whats': [6, 8],
                },
                dict[str, list[int]],
                None,
            ),
        ],
    )
    def test_raise_for(
        self, value: Any, type_: Any, exception: TypeError
    ) -> None:
        TypeChecker.raise_for(value, type_)
