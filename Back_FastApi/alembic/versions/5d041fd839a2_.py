"""empty message

Revision ID: 5d041fd839a2
Revises: db410ca4c557
Create Date: 2024-03-22 10:12:09.743132

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5d041fd839a2'
down_revision = 'db410ca4c557'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_categories',
                    sa.Column('id_product_category', sa.Integer(), nullable=False),
                    sa.Column('name_of_category', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id_product_category')
                    )
    op.create_table('transactions',
                    sa.Column('id_transaction', sa.Integer(), nullable=False),
                    sa.Column('id_product', sa.Integer(), nullable=False),
                    sa.Column('quantity', sa.Float(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('type', sa.Enum('output', 'input', 'event', 'return', name='transaction_type_enum',
                                              create_constraint=True), nullable=False),
                    sa.Column('create_date', sa.DateTime(timezone=True), server_default=sa.text('now()'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id_transaction')
                    )
    op.create_table('units',
                    sa.Column('id_unit', sa.Integer(), nullable=False),
                    sa.Column('unit', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id_unit')
                    )
    op.create_table('products',
                    sa.Column('id_product', sa.Integer(), nullable=False),
                    sa.Column('id_units', sa.Integer(), nullable=False),
                    sa.Column('id_product_category', sa.Integer(), nullable=False),
                    sa.Column('name_of_product', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['id_product_category'], ['product_categories.id_product_category'], ),
                    sa.ForeignKeyConstraint(['id_units'], ['units.id_unit'], ),
                    sa.PrimaryKeyConstraint('id_product')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('units')
    op.drop_table('transactions')
    op.drop_table('product_categories')
    # ### end Alembic commands ###
