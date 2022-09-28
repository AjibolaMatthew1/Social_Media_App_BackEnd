"""create posts table

Revision ID: 72f9fd08187d
Revises: 
Create Date: 2022-09-27 13:58:47.608253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72f9fd08187d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))

    pass

def downgrade() -> None:
    op.drop_table('posts')

    pass
