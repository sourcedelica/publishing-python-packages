from numbers import Number
from typing import List


def harmonic_mean(ms: List[Number]) -> float:
    # noinspection PyTypeChecker
    return len(ms) / sum(1 / m for m in ms)
