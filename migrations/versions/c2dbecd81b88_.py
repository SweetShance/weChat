"""empty message

Revision ID: c2dbecd81b88
Revises: a570f50924a5
Create Date: 2021-03-20 17:28:05.270438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2dbecd81b88'
down_revision = 'a570f50924a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat_room', sa.Column('room_status', sa.SmallInteger(), nullable=True, comment='房间状态,0 未开始，1已开始'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat_room', 'room_status')
    # ### end Alembic commands ###