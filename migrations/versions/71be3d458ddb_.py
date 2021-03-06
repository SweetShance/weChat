"""empty message

Revision ID: 71be3d458ddb
Revises: e61ef99641f6
Create Date: 2021-03-20 16:53:19.524567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71be3d458ddb'
down_revision = 'e61ef99641f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('rooms_ibfk_1', 'rooms', type_='foreignkey')
    op.create_foreign_key(None, 'rooms', 'users', ['user_id'], ['union_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rooms', type_='foreignkey')
    op.create_foreign_key('rooms_ibfk_1', 'rooms', 'users', ['user_id'], ['union_id'], ondelete='CASCADE')
    # ### end Alembic commands ###
