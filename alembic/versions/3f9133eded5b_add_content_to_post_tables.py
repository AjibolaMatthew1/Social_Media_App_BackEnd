"""add content to post tables

Revision ID: 3f9133eded5b
Revises: 72f9fd08187d
Create Date: 2022-09-27 14:20:00.510969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f9133eded5b'
down_revision = '72f9fd08187d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
