"""Initial Migration

Revision ID: 800456c24ab2
Revises: 946cd73643e0
Create Date: 2020-07-17 00:16:46.158637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '800456c24ab2'
down_revision = '946cd73643e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###