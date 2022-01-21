import sys

import pytest
from termcolor import colored

from imppkg.harmony import main


@pytest.mark.parametrize(
    ('inputs', 'expected'),
    [
        (['1', '4', '4'], 2.0),  # Happy path
        (['a', 'b'], 0.0),  # Bad input
        ([], 0.0),  # No input
    ],
)
def test_harmony_parameterized(monkeypatch, capsys, inputs, expected):
    monkeypatch.setattr(sys, 'argv', ['harmony'] + inputs)

    main()

    assert capsys.readouterr().out.strip() == colored(
        str(expected), 'red', 'on_cyan', attrs=['bold']
    )
