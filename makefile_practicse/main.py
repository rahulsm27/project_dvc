import black
import numpy
import pytest


def add_two_integers(a: int, b: int) -> int:
    return a + b


def add_two_floats(a: float, b: float) -> float:
    return a + b


def concatenate_two_strings(a: str, b: str) -> str:
    return a + b


def main() -> None:
    print(add_two_integers(1, 2))
    print(add_two_floats(1.0, 2.0))
    print(concatenate_two_strings("hello", "world"))

    # MYpy erros
    print(add_two_integers(1.0, 2.0))
    print(add_two_floats("1", 2))
    print(concatenate_two_strings(1, 2))


if __name__ == "__main__":
    main()
