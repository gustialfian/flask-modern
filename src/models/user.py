from sqlalchemy import Column, Integer, String
from src.database import Base
from src.serialize import ma


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
