from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    Text,
    Date,
)

from .meta import Base


class ProductComment(Base):
    __tablename__ = 'product_comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"))
    author_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    text = Column(Text)
    rating = Column(SmallInteger)
    publish_date = Column(Date)


Index('product_coment_product_id_ind', ProductComment.product_id, mysql_length=255)
Index('product_coment_author_id_ind', ProductComment.author_id, mysql_length=255)
