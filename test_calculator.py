import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Фикстура: создаёт экземпляр калькулятора перед каждым тестом."""
    return Calculator()


# =========================================================
# Тесты для add()
# =========================================================

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (-5, -3, -8),
    (100, 200, 300),
    (2.5, 3.5, 6.0),
])
def test_add(calc, a, b, expected):
    """Параметризованный тест сложения."""
    assert calc.add(a, b) == expected


# =========================================================
# Тесты для subtract()
# =========================================================

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
    (-1, -1, 0),
    (10.5, 0.5, 10.0),
])
def test_subtract(calc, a, b, expected):
    """Параметризованный тест вычитания."""
    assert calc.subtract(a, b) == expected


# =========================================================
# Тесты для multiply()
# =========================================================

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-2, 3, -6),
    (-2, -3, 6),
    (0.5, 4, 2.0),
])
def test_multiply(calc, a, b, expected):
    """Параметризованный тест умножения."""
    assert calc.multiply(a, b) == expected


# =========================================================
# Тесты для divide()
# =========================================================

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (-8, 2, -4.0),
    (1, 4, 0.25),
    (0, 5, 0.0),
])
def test_divide_positive(calc, a, b, expected):
    """Параметризованный позитивный тест деления."""
    assert calc.divide(a, b) == expected


def test_divide_by_zero_raises_value_error(calc):
    """Негативный тест: деление на ноль должно бросать ValueError."""
    with pytest.raises(ValueError) as exc_info:
        calc.divide(10, 0)
    assert "Деление на ноль" in str(exc_info.value)


def test_divide_zero_by_zero_raises(calc):
    """Негативный тест: 0 / 0 тоже должно бросать ValueError."""
    with pytest.raises(ValueError):
        calc.divide(0, 0)


# =========================================================
# Тесты для is_prime_number()
# =========================================================

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (19, True),
    (23, True),
    (97, True),
])
def test_is_prime_number_true(calc, n, expected):
    """Числа, которые являются простыми."""
    assert calc.is_prime_number(n) == expected


@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, False),
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
    (15, False),
    (100, False),
    (-7, False),
])
def test_is_prime_number_false(calc, n, expected):
    """Числа, которые НЕ являются простыми."""
    assert calc.is_prime_number(n) == expected


def test_is_prime_number_with_float_raises_type_error(calc):
    """Негативный тест: передача float должна бросать TypeError."""
    with pytest.raises(TypeError) as exc_info:
        calc.is_prime_number(3.5)
    assert "целым" in str(exc_info.value)


def test_is_prime_number_with_string_raises_type_error(calc):
    """Негативный тест: передача строки должна бросать TypeError."""
    with pytest.raises(TypeError):
        calc.is_prime_number("пять")