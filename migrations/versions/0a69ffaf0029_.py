"""empty message

Revision ID: 0a69ffaf0029
Revises: 1f436c263db7
Create Date: 2024-03-07 00:41:25.094101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a69ffaf0029'
down_revision = '1f436c263db7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
