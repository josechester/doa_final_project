from source.Car import Car
import pytest


class TestClass:

    @pytest.fixture(scope='function')
    def prius(self):
        return Car("Prius", "2004", "white")

    def test_condition(self, prius):
        assert prius.condition() == "New"

    def test_drive(self, prius):
        prius.drive(1000)
        assert prius.mileage == 1000

    def test_description(self, prius):
        prius.drive(1000)
        assert prius.condition() == "Used"
