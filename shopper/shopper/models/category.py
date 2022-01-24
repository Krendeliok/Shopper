from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
    String,
)

from .meta import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50))


Index('category_category_name_ind', Category.category_name, mysql_length=255)
