import datetime as dt
from typing import get_args
from sqlalchemy import ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql import func

from core.db_src.db_models.base_models import Base
from core.db_src.schemas.product_schemas import TransactionEnum


class ProductModel(Base):
    __tablename__ = 'products'

    id_product: Mapped[int] = mapped_column(primary_key=True)
    id_units: Mapped[int] = mapped_column(ForeignKey("units.id_unit"))
    id_product_category: Mapped[int] = mapped_column(ForeignKey("product_categories.id_product_category"))
    name_of_product: Mapped[str] = mapped_column(nullable=False, default="")

    product__unit = relationship("UnitModel", back_populates="unit__product")
    product__product_category = relationship("ProductCategoryModel", back_populates="product_category__product")
    product__transaction = relationship("TransactionModel", back_populates="transaction__product")
    product__meal = relationship("MealModel", back_populates="meal__product")


class ProductCategoryModel(Base):
    __tablename__ = 'product_categories'

    id_product_category: Mapped[int] = mapped_column(primary_key=True)
    name_of_category: Mapped[str] = mapped_column(nullable=False, default="")

    product_category__product = relationship("ProductModel", back_populates="product__product_category")


class UnitModel(Base):
    __tablename__ = 'units'

    id_unit: Mapped[int] = mapped_column(primary_key=True)
    unit: Mapped[str] = mapped_column(nullable=False, default="")

    unit__product = relationship("ProductModel", back_populates="product__unit")


class TransactionModel(Base):
    __tablename__ = 'transactions'

    id_transaction: Mapped[int] = mapped_column(primary_key=True)
    id_product: Mapped[int] = mapped_column(ForeignKey("products.id_product"), nullable=False, default=0)
    quantity: Mapped[float] = mapped_column(nullable=False, default=1)
    price: Mapped[float] = mapped_column(nullable=False, default=0)
    type: Mapped[TransactionEnum] = mapped_column(Enum(
        *get_args(TransactionEnum),
        name="transaction_type_enum",
        create_constraint=True,
        validate_strings=True,
    ))
    create_date: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    transaction__product = relationship("ProductModel", back_populates="product__transaction")
