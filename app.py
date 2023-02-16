# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение


from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


# функция создания основного объекта app
def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(applicaition):
    db.init_app(applicaition)
    api = Api(applicaition)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


# def load_data():
#     with app.app_context():
#         db.session.commit()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)
    # load_data()

    app.run(host="localhost", port=10001)
