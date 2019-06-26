from main import or_and, notperceptron, perceptron_xor, perceptron_xnor
import pytest

@pytest.mark.parametrize("th0", list(range(1, 5)))
@pytest.mark.parametrize("th1", list(range(-40, -25)))
def test_not(th0, th1):
    assert perceptron_not([0, 1], [th0, th1]) == [1, 0]
