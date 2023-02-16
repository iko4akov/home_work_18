# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.


# Пример
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.dao.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')


        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.dao.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        elif 'description' in data:
            movie.description = data.get('description')
        elif 'trailer' in data:
            movie.trailer = data.get('trailer')
        elif 'year' in data:
            movie.year = data.get('year')
        elif 'rating' in data:
            movie.rating = data.get('rating')
        elif 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        elif 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
