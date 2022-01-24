from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
)

from .meta import Base


class OrderDetail(Base):
    __tablename__ = 'order_detail'
    order_id = Column(Integer, ForeignKey("order.id", ondelete="CASCADE"), primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"), primary_key=True)


Index('order_detail_order_id_ind', OrderDetail.order_id, mysql_length=255)
Index('order_detail_product_id_ind', OrderDetail.product_id, mysql_length=255)
