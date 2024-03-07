from sqlalchemy import Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from db_src.db_models.base_model import Base
import datetime as dt


class ProductModel:
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    discount_id = Column(Integer, ForeignKey("discounts.discount_id"))
    product_name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(String, nullable=False)

    items_in_cart = relationship("CartModel", back_populates="product")


class DiscountModel:
    __tablename__ = 'discounts'

    discount_id = Column(Integer, primary_key=True)
    discount_percentage = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow)
    ended_at = Column(DateTime, nullable=False)

    products = relationship("ProductModel")
