from marshmallow import Schema, fields

from database import db


class Favorite(db.Model):
    __tablename__ = 'favorite'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    movie = db.relationship('Movie')


class FavoriteSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer()
    movie_id = fields.Integer()
