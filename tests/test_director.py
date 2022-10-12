import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from unittest.mock import MagicMock

from service.director import DirectorService


@pytest.fixture
def director_dao():
    director = DirectorDAO(None)
    director_one = Director(id=1, name="director_one")
    director_two = Director(id=2, name="director_two")

    director.get_one = MagicMock(return_value=director_one)
    director.get_all = MagicMock(return_value=[director_one, director_two])
    director.create = MagicMock(return_value=director_one)
    director.delete = MagicMock(return_value=True)
    director.create = MagicMock(return_value=True)

    return director


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(2).name == "director_one"
        assert self.director_service.get_one(1) is not None

    def test_get_all(self):
        assert self.director_service.get_all() is not None
        assert len(self.director_service.get_all()) == 2

    def test_create(self):
        assert self.director_service.create(1) is True

    def test_delete(self):
        assert self.director_service.delete(1) is True

    def test_update(self):
        assert self.director_service.update(1) is True

