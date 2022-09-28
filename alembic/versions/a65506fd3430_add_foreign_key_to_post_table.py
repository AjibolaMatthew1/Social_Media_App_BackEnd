"""add foreign key to post table

Revision ID: a65506fd3430
Revises: 9f3f95cad6f2
Create Date: 2022-09-28 12:50:45.232260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a65506fd3430'
down_revision = '9f3f95cad6f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table="users", local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column("posts", "user_id")

    pass
