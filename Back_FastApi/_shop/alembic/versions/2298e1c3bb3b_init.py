"""init users

Revision ID: 2298e1c3bb3b
Revises: 
Create Date: 2022-12-09 18:18:10.505777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2298e1c3bb3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('email', sa.Unicode(81), nullable=False, unique=True),
        sa.Column('hashed_password', sa.Unicode, nullable=False),
        sa.Column('is_employee', sa.Boolean, nullable=False),
        sa.Column('is_admin', sa.Boolean, nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),

        sa.Column('telephone', sa.Integer, nullable=False),
        sa.Column('first_name', sa.Unicode(51), nullable=False),
        sa.Column('last_name', sa.Unicode(81), nullable=False),
        sa.Column('post_code', sa.Integer, nullable=False),
        sa.Column('street_name', sa.Unicode(301), nullable=False),
        sa.Column('street_number', sa.Integer, nullable=False),
        sa.Column('flat_number', sa.Integer, nullable=False),
    )
    # ut = 'users'
    # op.add_column(ut, sa.Column('hashed_password', sa.String, nullable=False))
    # op.alter_column(ut, 'password', new_column_name='hashed_password')


def downgrade() -> None:
    op.drop_table('users')
