from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
)

from .meta import Base


class Basket(Base):
    __tablename__ = 'basket'
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"), primary_key=True)


Index('basket_product_id_ind', Basket.product_id, mysql_length=255)
Index('basket_user_id_ind', Basket.user_id, mysql_length=255)
