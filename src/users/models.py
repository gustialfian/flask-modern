from sqlalchemy import Column, Integer, String

from src.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String())
    password = Column(String())

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User {}>".format(self.name)
