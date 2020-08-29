from sqlalchemy import Column, Integer, String

from src.database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Item {}>".format(self.name)
