import pytest
from dao.movie import MovieDAO
from dao.model.movie import Movie
from unittest.mock import MagicMock

from service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie = MovieDAO(None)
    movie_one = Movie(
        id=1,
        title="title_one",
        description="description_one",
        trailer="trailer_one",
        year=1996,
        rating=5.1,
        genre_id=1,
        director_id=1
    )
    movie_two = Movie(
        id=2,
        title="title_two",
        description="description_two",
        trailer="trailer_two",
        year=1996,
        rating=5.1,
        genre_id=1,
        director_id=1
    )

    movie.get_one = MagicMock(return_value=movie_one)
    movie.get_all = MagicMock(return_value=[movie_one, movie_two])
    movie.create = MagicMock(return_value=movie_one)
    movie.delete = MagicMock(return_value=True)
    movie.create = MagicMock(return_value=True)

    return movie


class TestMovieDao:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) == "movie_one"
        assert self.movie_service.get_one(1) is not None

    def test_get_all(self):
        assert self.movie_service.get_all() is not None
        assert len(self.movie_service.get_all()) == 2

    def test_create(self):
        assert self.movie_service.create(1) is True

    def test_delete(self):
        assert self.movie_service.delete(1) is True

    def test_update(self):
        assert self.movie_service.update(1) is True