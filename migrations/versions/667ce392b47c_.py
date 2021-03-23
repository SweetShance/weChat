"""empty message

Revision ID: 667ce392b47c
Revises: d674bdeb01d1
Create Date: 2021-03-20 17:01:55.879638

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '667ce392b47c'
down_revision = 'd674bdeb01d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('union_id', sa.BigInteger(), autoincrement=True, nullable=False, comment='聊天室id'),
    sa.Column('room_name', sa.VARCHAR(length=20), nullable=False, comment='聊天室名字'),
    sa.Column('user_id', sa.BigInteger(), nullable=False, comment='房间主人id'),
    sa.Column('describe', sa.VARCHAR(length=500), nullable=True, comment='房间简介'),
    sa.Column('sid', sa.VARCHAR(length=100), nullable=True, comment='房间sid'),
    sa.Column('number', sa.VARCHAR(length=7), nullable=False, comment='房间编号, 1356879'),
    sa.Column('room_status', sa.SmallInteger(), nullable=True, comment='房间状态,0 未开始，1已开始'),
    sa.Column('create_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.union_id'], ),
    sa.PrimaryKeyConstraint('union_id'),
    sa.UniqueConstraint('number'),
    sa.UniqueConstraint('room_name'),
    sa.UniqueConstraint('user_id')
    )
    op.drop_index('number', table_name='rooms')
    op.drop_index('room_name', table_name='rooms')
    op.drop_index('user_id', table_name='rooms')
    op.drop_table('rooms')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rooms',
    sa.Column('union_id', mysql.BIGINT(), autoincrement=True, nullable=False, comment='聊天室id'),
    sa.Column('room_name', mysql.VARCHAR(length=20), nullable=False, comment='聊天室名字'),
    sa.Column('user_id', mysql.BIGINT(), autoincrement=False, nullable=False, comment='房间主人id'),
    sa.Column('describe', mysql.VARCHAR(length=500), nullable=True, comment='房间简介'),
    sa.Column('sid', mysql.VARCHAR(length=100), nullable=True, comment='房间sid'),
    sa.Column('number', mysql.VARCHAR(length=7), nullable=False, comment='房间编号, 1356879'),
    sa.Column('room_status', mysql.SMALLINT(), autoincrement=False, nullable=True, comment='房间状态,0 未开始，1已开始'),
    sa.Column('create_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('update_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.union_id'], name='rooms_ibfk_1'),
    sa.PrimaryKeyConstraint('union_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('user_id', 'rooms', ['user_id'], unique=True)
    op.create_index('room_name', 'rooms', ['room_name'], unique=True)
    op.create_index('number', 'rooms', ['number'], unique=True)
    op.drop_table('room')
    # ### end Alembic commands ###
