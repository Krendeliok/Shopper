from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String
)

from .meta import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    surname = Column(Text)
    email = Column(Text, unique=True)
    phone = Column(String(15))
    password = Column(String)


Index('user_email_ind', User.email, unique=True, mysql_length=255)
