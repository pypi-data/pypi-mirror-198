import pytest
import argparse
import mock
from src.single_chars_counter_package.single_chars_counter import single_chars_counter as counter, main, read_file


def test_counter_typical():
    cases = [
        ('abbbccdf', 3),
        ('abcd', 4),
        ('ab c', 4),
        ('', 0)
    ]
    for text, count in cases:
        assert counter(text) == count


def test_counter_atypical():
    with pytest.raises(TypeError) as e:
        counter(4)
    assert "The function accepts only 'str' type, got <class 'int'>" == e.value.args[0]


def test_read_file(tmp_path):
    test_file = tmp_path / 'test.txt'
    test_file.write_text("test read file")

    assert read_file(test_file) == "test read file"


@mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
    file="file path", string="string argument"))
def test_main(mock_args, monkeypatch):
    def mock_read_file(arg):
        return arg

    monkeypatch.setattr('single_chars_counter_package.single_chars_counter_package.read_file', mock_read_file)

    def mock_counter(arg):
        return arg

    monkeypatch.setattr('single_chars_counter_package.single_chars_counter_package.single_chars_counter_package', mock_counter)

    assert main() == "file path"


if __name__ == '__main__':
    pytest.main()
