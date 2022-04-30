"""add content column to post table

Revision ID: a0271ad16a1a
Revises: ff7a9c704dab
Create Date: 2022-04-24 19:57:17.947864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a0271ad16a1a"
down_revision = "ff7a9c704dab"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
