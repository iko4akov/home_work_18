from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):

        if request.args.get("director_id"):
            dir_id = request.args.get("director_id")
            movie_query = movie_service.mov_by_dir(dir_id)
            return movies_schema.dump(movie_query), 200

        elif request.args.get("genre_id"):
            gen_id = request.args.get("genre_id")
            movie_query = movie_service.mov_by_gen(gen_id)
            return movies_schema.dump(movie_query), 200

        elif request.args.get("year"):
            year = request.args.get("year")
            movie_query = movie_service.mov_by_year(year)
            return movies_schema.dump(movie_query), 200

        elif request.args.get("genre_id") and request.args.get("director_id"):
            gen_id = request.args.get("genre_id")
            dir_id = request.args.get("director_id")
            movie_query = movie_service.mov_by_dir_gen(gen_id, dir_id)
            return movies_schema.dump(movie_query), 200
        else:
            all_movie = movie_service.get_all()
            return movies_schema.dump(all_movie), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie)

        except Exception:

            return "", 404

    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update(req_json)

        return "", 204

    def patch(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)

        return "", 204
