import pytest


@pytest.mark.skip(reason="Фича в разработке")
def test_feature_in_development():
    pass


@pytest.mark.skip(reason="Фича в разработке")
class TestSuiteSkip:
    def test_1(self):
        pass

    def test_2(self):
        pass
