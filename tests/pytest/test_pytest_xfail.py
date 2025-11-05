import pytest


@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг исправлен")
def test_without_bug():
    pass
