from typing import Sequence, SupportsFloat


# Logged https://youtrack.jetbrains.com/issue/PY-52641 for type checker bug
# But it passes mypy

def harmonic_mean(ms: Sequence[SupportsFloat]) -> float:
    # noinspection PyTypeChecker
    return len(ms) / sum(1 / m for m in ms)
