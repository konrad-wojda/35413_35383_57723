from sqlalchemy import ForeignKey,  UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column, Mapped

from core.db_src.db_models.base_models import Base


class MealModel(Base):
    __tablename__ = 'meals'

    id_meal: Mapped[int] = mapped_column(primary_key=True)
    id_product: Mapped[int] = mapped_column(ForeignKey("products.id_product"))
    id_school: Mapped[int] = mapped_column(ForeignKey("schools.id_school"))
    id_meal_type: Mapped[int] = mapped_column(ForeignKey("meal_types.id_meal_type"))
    date: Mapped[str] = mapped_column(nullable=False, default="")

    meal__product = relationship("ProductModel", back_populates="product__meal")
    meal__school = relationship("SchoolModel", back_populates="school__meal")
    meal__meal_type = relationship("MealTypeModel", back_populates="meal_type__meal")

    UniqueConstraint('id_product', 'id_school', 'id_meal_type', 'date', name=f'uq_{__tablename__}_all')


class MealRuleModel(Base):
    __tablename__ = 'meal_rules'

    id_student: Mapped[int] = mapped_column(ForeignKey("students.id_student"), primary_key=True)
    id_meal_type: Mapped[int] = mapped_column(ForeignKey("meal_types.id_meal_type"), primary_key=True)

    meal_rule__student = relationship("StudentModel", back_populates="student__meal_rule")
    meal_rule__meal_type = relationship("MealTypeModel", back_populates="meal_type__meal_rule")


class MealTypeModel(Base):
    __tablename__ = 'meal_types'

    id_meal_type: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False, default="")

    meal_type__meal_rule = relationship("MealRuleModel", back_populates="meal_rule__meal_type")
    meal_type__attendance_list = relationship("AttendanceListModel", back_populates="attendance_list__meal_type")
    meal_type__meal = relationship("MealModel", back_populates="meal__meal_type")

    UniqueConstraint('id_student', 'id_meal_type', name=f'uq_{__tablename__}__id_student_id_meal_type')
