from calculon.calculator import calculate_expression

def test_addition(capsys):
    calculate_expression("2 + 3")
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out
