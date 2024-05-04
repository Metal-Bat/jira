from random import randint


def generate_random_login_code(length: int = 5) -> int:
    """generate login code with allowing length change

    Args:
        length (int, optional): length of random number. Defaults to 5.

    Returns:
        int: the random number with specific length

    >>> from app.users.utils import generate_random_login_code
    >>> random_code: int = generate_random_login_code()
    >>> result: bool = 9999 < random_code < 100000
    >>> result
    True

    """
    start_point: int = int("1" * length)
    end_point: int = int("9" * length)
    code: int = randint(start_point, end_point)
    return code
