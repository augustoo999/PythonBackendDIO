import pytest
from src.utils import eleva_quadrado


@pytest.mark.parametrize("test_input, expected", [(2, 4), (10, 100), (3, 9)])
def test_eleva_quadrado(test_input, expected):
    resultado = eleva_quadrado(test_input)
    assert resultado == expected


@pytest.mark.parametrize(
    "test_input, exc_class, msg",
    [
        (
            "a",
            TypeError,
            "unsupported operand type(s) for ** or pow(): 'str' and 'int'",
        ),
        (
            None,
            TypeError,
            "unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'",
        ),
    ],
)
def test_eleva_quadrado_fail(test_input, exc_class, msg):
    with pytest.raises(exc_class) as exc:
        eleva_quadrado(test_input)
    assert str(exc.value) == msg
