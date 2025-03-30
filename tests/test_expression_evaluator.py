import pytest
from ..postfix import evaluate_expression  # Импорт вашей функции

class TestExpressionEvaluator:
    def test_simple_addition(self):
        assert evaluate_expression("2 + 3") == 5

    def test_complex_expression(self):
        assert evaluate_expression("(10 - 2) * 3") == 24

    def test_invalid_syntax(self):
        with pytest.raises(SyntaxError):
            evaluate_expression("2 + * 3")
