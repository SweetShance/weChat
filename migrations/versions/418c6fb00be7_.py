"""empty message

Revision ID: 418c6fb00be7
Revises: 4b36bc623865
Create Date: 2021-03-20 17:17:19.794820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418c6fb00be7'
down_revision = '4b36bc623865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat_room',
    sa.Column('union_id', sa.BigInteger(), autoincrement=True, nullable=False, comment='聊天室id'),
    sa.PrimaryKeyConstraint('union_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chat_room')
    # ### end Alembic commands ###