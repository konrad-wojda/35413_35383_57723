from typing import List
from passlib import hash as pswrd_hash
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from core.db_src.db_models.base_models import Base


class SchoolModel(Base):
    __tablename__ = "schools"
#
    id_school: Mapped[int] = mapped_column(primary_key=True)
    name_of_school: Mapped[str] = mapped_column(nullable=False, default="")
    post_code: Mapped[int] = mapped_column(nullable=False, default=0)
    street_name: Mapped[str] = mapped_column(nullable=False, default="")
    street_number: Mapped[int] = mapped_column(nullable=False, default=0)

    school__intendant: Mapped[List["IntendantModel"]] = relationship("IntendantModel",
                                                                     back_populates="intendant__school")
    school__student: Mapped[List["StudentModel"]] = relationship("StudentModel",
                                                                 back_populates="student__school")
    school__meal: Mapped[List["MealModel"]] = relationship("MealModel",
                                                           back_populates="meal__school")


class UserModel(Base):
    __tablename__ = "users"

    id_user: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    first_name: Mapped[str] = mapped_column(nullable=False, default="")
    last_name: Mapped[str] = mapped_column(nullable=False, default="")

    user__intendant: Mapped["IntendantModel"] = relationship("IntendantModel", back_populates="intendant__user")

    def __str__(self):
        return f'{self.id_user}: {self.email}'

    def verify_password(self, password: str) -> bool:
        """
        Checks if encrypted password matches hashed password from DB
        :param password: password putted in input
        :return: True if matches / False if not matches
        """
        return pswrd_hash.bcrypt.verify(password, self.hashed_password)


class IntendantModel(Base):
    __tablename__ = "intendants"

    id_intendant: Mapped[int] = mapped_column(primary_key=True)
    is_main_admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"))
    id_school: Mapped[int] = mapped_column(ForeignKey("schools.id_school"))

    intendant__user: Mapped["UserModel"] = relationship("UserModel", back_populates="user__intendant")
    intendant__school: Mapped["SchoolModel"] = relationship("SchoolModel", back_populates="school__intendant")

    def __str__(self):
        return f'{self.id_intendant}: {self.is_main_admin}'
