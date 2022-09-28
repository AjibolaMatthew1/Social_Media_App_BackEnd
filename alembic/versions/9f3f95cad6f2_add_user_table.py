"""Add user table

Revision ID: 9f3f95cad6f2
Revises: 3f9133eded5b
Create Date: 2022-09-27 14:24:50.426653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f3f95cad6f2'
down_revision = '3f9133eded5b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default = sa.text('now()'), nullable=False),
    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
