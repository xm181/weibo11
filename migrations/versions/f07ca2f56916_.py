"""empty message

Revision ID: f07ca2f56916
Revises: 
Create Date: 2020-11-10 10:44:39.993146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f07ca2f56916'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('gender', sa.Enum('male', 'female', 'unknow'), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('city', sa.String(length=10), server_default='中国', nullable=True),
    sa.Column('avatar', sa.String(length=256), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
