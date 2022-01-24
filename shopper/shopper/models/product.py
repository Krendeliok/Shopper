from unicodedata import category
from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    Text,
    String
)

from .meta import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    price = Column(Integer)
    rating = Column(SmallInteger)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="RESTRICT"))


Index('product_product_name_ind', Product.product_name, unique=True, mysql_length=255)
