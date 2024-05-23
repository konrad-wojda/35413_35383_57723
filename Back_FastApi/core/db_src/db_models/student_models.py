from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from core.db_src.db_models.base_models import Base


class StudentModel(Base):
    __tablename__ = 'students'

    id_student: Mapped[int] = mapped_column(primary_key=True)
    id_school: Mapped[int] = mapped_column(ForeignKey("schools.id_school"))
    student_first_name: Mapped[int] = mapped_column(nullable=False, default="")
    student_last_name: Mapped[str] = mapped_column(nullable=False, default="")

    student__attendance_list = relationship("AttendanceListModel", back_populates="attendance_list__student")
    student__school = relationship("SchoolModel", back_populates="school__student")
    student__meal_rule = relationship("MealRuleModel", back_populates="meal_rule__student")


class AttendanceListModel(Base):
    __tablename__ = 'attendance_lists'

    id_attendance_list: Mapped[int] = mapped_column(primary_key=True)
    id_student: Mapped[int] = mapped_column(ForeignKey("students.id_student"))
    id_meal_type: Mapped[int] = mapped_column(ForeignKey("meal_types.id_meal_type"))
    date: Mapped[str] = mapped_column(nullable=False, default="")

    attendance_list__meal_type = relationship("MealTypeModel", back_populates="meal_type__attendance_list")
    attendance_list__student = relationship("StudentModel", back_populates="student__attendance_list")
