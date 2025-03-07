"""create lists table

Revision ID: 244b4ee9e033
Revises: 46fa2cf0b6fa
Create Date: 2024-12-12 00:31:06.955988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '244b4ee9e033'
down_revision = '46fa2cf0b6fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lists',
    sa.Column('user_id', sa.Integer, nullable=False),
    sa.Column('player_1', sa.String(length=40), nullable=True),
    sa.Column('player_2', sa.String(length=40), nullable=True),
    sa.Column('player_3', sa.String(length=40), nullable=True),
    sa.Column('player_4', sa.String(length=40), nullable=True),
    sa.Column('player_5', sa.String(length=40), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lists')
    # ### end Alembic commands ###
