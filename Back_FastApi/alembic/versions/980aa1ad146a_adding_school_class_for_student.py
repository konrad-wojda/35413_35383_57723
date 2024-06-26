"""adding school_class for student

Revision ID: 980aa1ad146a
Revises: 1624b2f813d5
Create Date: 2024-06-22 13:58:37.065987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980aa1ad146a'
down_revision = '1624b2f813d5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('_student_meal_date_uc', 'attendance_lists', ['id_student', 'id_meal_type', 'date'])
    op.add_column('students', sa.Column('student_class', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'student_class')
    op.drop_constraint('_student_meal_date_uc', 'attendance_lists', type_='unique')
    # ### end Alembic commands ###
