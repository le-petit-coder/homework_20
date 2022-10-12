import pytest
from dao.genre import GenreDAO
from dao.model.genre import Genre
from unittest.mock import MagicMock

from service.genre import GenreService


@pytest.fixture
def genre_dao():
    genre = GenreDAO(None)
    genre_one = Genre(id=1, name="genre_one")
    genre_two = Genre(id=2, name="genre_two")

    genre.get_one = MagicMock(return_value=genre_one)
    genre.get_all = MagicMock(return_value=[genre_one, genre_two])
    genre.create = MagicMock(return_value=genre_one)
    genre.delete = MagicMock(return_value=True)
    genre.create = MagicMock(return_value=True)

    return genre


class TestGenreDao:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        assert self.genre_service.get_one(2).name == "genre_one"
        assert self.genre_service.get_one(1) is not None

    def test_get_all(self):
        assert self.genre_service.get_all() is not None
        assert len(self.genre_service.get_all()) == 2

    def test_create(self):
        assert self.genre_service.create(1) is True

    def test_delete(self):
        assert self.genre_service.delete(1) is True

    def test_update(self):
        assert self.genre_service.update(1) is True

