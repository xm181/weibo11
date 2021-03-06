"""empty message

Revision ID: 3c909538fe7a
Revises: 117d9f3a76c3
Create Date: 2020-11-13 11:57:10.885671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c909538fe7a'
down_revision = '117d9f3a76c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('n_fans', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('n_follow', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'n_follow')
    op.drop_column('user', 'n_fans')
    # ### end Alembic commands ###
