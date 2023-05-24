"""Renaming column name to first_name

Revision ID: 2d20ce9271a8
Revises: 791279dd0760
Create Date: 2023-05-24 17:51:58.799249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d20ce9271a8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='first_name')


def downgrade() -> None:
    op.alter_column('students', 'first_name', new_column_name='name')
