from collections import Counter
from functools import lru_cache
from argparse import ArgumentParser, Namespace


@lru_cache(maxsize=128)
def single_chars_counter(input_str: str) -> int:
    """
    The function takes a string and returns the number of characters
    in the string occurring only once.
    :param: input_str:input string
    :return: quantity of the single chars
    """
    if not isinstance(input_str, str):
        raise TypeError(f"The function accepts only 'str' type, got {type(input_str)}")
    return sum(num for num in Counter(input_str).values() if num == 1)


def read_file(path: str) -> str:
    with open(path) as file_path:
        return file_path.read()


def main():
    parser = ArgumentParser()
    parser.add_argument('-s', '--string', type=str, help="To count single chars in your string.")
    parser.add_argument('-f', '--file', help="Path to file")
    args: Namespace = parser.parse_args()

    data = read_file(args.file) if args.file else args.string
    return single_chars_counter(data)


if __name__ == '__main__':
    print(main())
