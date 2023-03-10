from marshmallow import Schema, fields

from database import db


class Director(db.Model):
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
