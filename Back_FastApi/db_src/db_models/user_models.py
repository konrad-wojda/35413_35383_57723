from sqlalchemy import Integer, String, DateTime, Boolean, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from passlib import hash as pswrd_hash
from db_src.db_models.base_model import Base
import datetime as dt


class UserModel(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)  # index
    hashed_password = Column(String, nullable=False)
    is_employee = Column(Boolean, nullable=False, default=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow)
    telephone = Column(Integer, nullable=False, default=0)
    first_name = Column(String, nullable=False, default="")
    last_name = Column(String, nullable=False, default="")
    post_code = Column(Integer, nullable=False, default=0)
    street_name = Column(String, nullable=False, default="")
    street_number = Column(Integer, nullable=False, default=0)
    flat_number = Column(Integer, nullable=False, default=0)

    # items_in_cart = relationship("CartModel", back_populates="user")
    # payments_history = relationship("PaymentHistoryModel", back_populates="payments_history")

    def __str__(self):
        return f'{self.user_id}: {self.email}'

    def verify_password(self, password: str):
        return pswrd_hash.bcrypt.verify(password, self.hashed_password)


Index('user_index', UserModel.email)
