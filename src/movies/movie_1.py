from typing import Any

from movies.movie import Movie


class MovieLister:
    _finder: Any

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
    lister = MovieLister()
    spiderman_movies = lister.movies_directed_by("Spiderman")
    print(spiderman_movies)
