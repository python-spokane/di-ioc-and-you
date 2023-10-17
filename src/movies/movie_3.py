from typing import Protocol

from movies.movie import Movie


class MovieFinder(Protocol):
    def findAll(self) -> list[Movie]:
        ...


class ColonDelimitedMovieFinder:
    def __init__(self, filename: str):
        self._filename = filename

    def findAll(self) -> list[Movie]:
        movies: list[Movie] = []
        with open(self._filename) as fin:
            lines = fin.readlines()
            for line in lines:
                line = line.strip()
                title, director = tuple(line.split(":", maxsplit=1))
                movies.append(Movie(title, director))
        return movies


class MovieLister:
    _finder: MovieFinder

    def __init__(self, finder: MovieFinder): # <---------
        self._finder = finder

    def movies_directed_by(self, arg: str) -> list[Movie]:
        allMovies: list[Movie] = self._finder.findAll()
        movies = [
            movie
            for movie
            in allMovies
            if movie.director == arg
        ]
        return movies


if __name__ == "__main__":
    finder: MovieFinder = ColonDelimitedMovieFinder(filename="movies.txt")
    lister = MovieLister(finder)
    spiderman_movies = lister.movies_directed_by("Spiderman")
    print(spiderman_movies)
