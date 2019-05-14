"""followers

Revision ID: 489930d9904d
Revises: 71e715e83b14
Create Date: 2019-05-14 14:32:42.892000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489930d9904d'
down_revision = '71e715e83b14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
