"""empty message

Revision ID: 29fb0ec3b24f
Revises: c9e46ff8770e
Create Date: 2021-03-20 17:25:03.364386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29fb0ec3b24f'
down_revision = 'c9e46ff8770e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat_room', sa.Column('create_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('chat_room', sa.Column('update_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat_room', 'update_at')
    op.drop_column('chat_room', 'create_at')
    # ### end Alembic commands ###
