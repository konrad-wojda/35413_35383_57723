from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from db_src.db_models.base_model import Base
import datetime as dt


class CartModel:
    __tablename__ = 'items_in_cart'

    item_in_cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))  # index
    product_id = Column(Integer, ForeignKey("products.product_id"))
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=True)  # index
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow)

    order = relationship("OrderModel", back_populates="items_in_cart")
    user = relationship("UserModel", back_populates="items_in_cart")
    product = relationship("ProductModel", back_populates="items_in_cart")


class OrderModel:
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    payment_id = Column(Integer, ForeignKey("payments_history.payment_id"))
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow)

    payment = relationship("PaymentHistoryModel", back_populates="order")
    items_in_cart = relationship("CartModel", back_populates="order")


class PaymentHistoryModel:
    __tablename__ = 'payments_history'

    payment_id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    modified_at = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    order = relationship("OrderModel", back_populates="payment", uselist=False)
    user = relationship("UserModel", back_populates="payments_history")
    
