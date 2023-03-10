from database import db
from dao.movie_dao import MovieDAO
from service.movie_service import MovieService
from dao.genre_dao import GenreDAO
from service.genre_service import GenreService
from dao.director_dao import DirectorDAO
from service.director_service import DirectorService
from dao.user_dao import UserDAO
from service.user_service import UserService
from service.auth_service import AuthService
from dao.favorite_dao import FavoriteDAO
from service.favorite_service import FavoriteService

movie_dao = MovieDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
user_dao = UserDAO(session=db.session)
favorite_dao = FavoriteDAO(session=db.session)

movie_service = MovieService(dao=movie_dao)
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
favorite_service = FavoriteService(dao=favorite_dao)
