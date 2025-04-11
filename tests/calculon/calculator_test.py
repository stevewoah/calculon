import pytest
from calculon.calculator import calculate_expression, validate_args


def test_validate_args_valid():
    args = list(["1", "+", "3"])

    print(validate_args(args))

    assert validate_args(args) == "1 + 3"


def test_validate_args_invalid():
    args = list([])

    with pytest.raises(SystemExit) as e:
        validate_args(args)
    assert e.type == SystemExit
    assert e.value.code == 1


def test_addition(capsys):
    calculate_expression("2 + 3")
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out
