from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
)

from .meta import Base


class Favorite(Base):
    __tablename__ = 'favorite'
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"), primary_key=True)


Index('favorite_product_id_ind', Favorite.product_id, mysql_length=255)
Index('favorite_user_id_ind', Favorite.user_id, mysql_length=255)
