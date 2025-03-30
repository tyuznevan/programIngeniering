import pytest
import sys

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Автоматически найдёт корень

from postfix import evaluate_expression

class TestExpressionEvaluator:
    def test_simple_addition(self):
        assert evaluate_expression("2 + 3") == 5

    def test_complex_expression(self):
        assert evaluate_expression("(10 - 2) * 3") == 24

    def test_invalid_syntax(self):
        with pytest.raises(SyntaxError):
            evaluate_expression("2 + * 3")
