import os
import sys

from termcolor import colored

from imppkg.harmonic_mean import harmonic_mean
from imppkg.harmony import main


def test_harmony_happy_path(monkeypatch, capsys):
    inputs = ["1", "4", "4"]
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    main()

    expected_value = 2.0
    assert capsys.readouterr().out.strip() == colored(
        str(expected_value),
        "red",
        "on_cyan",
        attrs=["bold"]
    )


def test_harmony_no_inputs(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["harmony"])

    main()

    expected_value = 0.0
    assert capsys.readouterr().out.strip() == colored(
        str(expected_value),
        "red",
        "on_cyan",
        attrs=["bold"]
    )


def test_harmony_bad_inputs(monkeypatch, capsys):
    inputs = ["a", "b"]
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    main()

    expected_value = 0.0
    assert capsys.readouterr().out.strip() == colored(
        str(expected_value),
        "red",
        "on_cyan",
        attrs=["bold"]
    )
