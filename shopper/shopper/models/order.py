from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
)

from .meta import Base


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))


Index('order_user_id_ind', Order.user_id, mysql_length=255)
