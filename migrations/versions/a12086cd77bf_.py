"""empty message

Revision ID: a12086cd77bf
Revises: 3b3a1c6bd3d2
Create Date: 2023-05-29 17:25:20.455883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a12086cd77bf'
down_revision = '3b3a1c6bd3d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('birth_year', sa.String(length=20), nullable=False),
    sa.Column('eye_color', sa.String(length=20), nullable=False),
    sa.Column('skin_color', sa.String(length=20), nullable=False),
    sa.Column('hair_color', sa.String(length=20), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('people')
    # ### end Alembic commands ###