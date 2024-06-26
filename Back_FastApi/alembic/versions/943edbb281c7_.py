"""empty message

Revision ID: 943edbb281c7
Revises: 5d041fd839a2
Create Date: 2024-04-15 22:07:10.341832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '943edbb281c7'
down_revision = '5d041fd839a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meal_rules',
    sa.Column('id_student', sa.Integer(), nullable=False),
    sa.Column('id_meal_type', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_student', 'id_meal_type')
    )
    op.create_table('meal_types',
    sa.Column('id_meal_type', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id_meal_type')
    )
    op.create_table('attendance_lists',
    sa.Column('id_attendance_list', sa.Integer(), nullable=False),
    sa.Column('id_student', sa.Integer(), nullable=False),
    sa.Column('id_meal_type', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_meal_type'], ['units.id_unit'], ),
    sa.ForeignKeyConstraint(['id_student'], ['units.id_unit'], ),
    sa.PrimaryKeyConstraint('id_attendance_list')
    )
    op.create_table('students',
    sa.Column('id_student', sa.Integer(), nullable=False),
    sa.Column('id_school', sa.Integer(), nullable=False),
    sa.Column('student_first_name', sa.String(), nullable=False),
    sa.Column('student_last_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_school'], ['units.id_unit'], ),
    sa.PrimaryKeyConstraint('id_student')
    )
    op.create_table('meals',
    sa.Column('id_meal', sa.Integer(), nullable=False),
    sa.Column('id_product', sa.Integer(), nullable=False),
    sa.Column('id_school', sa.Integer(), nullable=False),
    sa.Column('id_meal_type', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_meal_type'], ['meal_types.id_meal_type'], ),
    sa.ForeignKeyConstraint(['id_product'], ['products.id_product'], ),
    sa.ForeignKeyConstraint(['id_school'], ['schools.id_school'], ),
    sa.PrimaryKeyConstraint('id_meal')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meals')
    op.drop_table('students')
    op.drop_table('attendance_lists')
    op.drop_table('meal_types')
    op.drop_table('meal_rules')
    # ### end Alembic commands ###
