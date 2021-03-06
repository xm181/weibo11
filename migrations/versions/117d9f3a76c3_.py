"""empty message

Revision ID: 117d9f3a76c3
Revises: f07ca2f56916
Create Date: 2020-11-12 08:36:08.963950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117d9f3a76c3'
down_revision = 'f07ca2f56916'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weibo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weibo_uid'), 'weibo', ['uid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_weibo_uid'), table_name='weibo')
    op.drop_table('weibo')
    # ### end Alembic commands ###
