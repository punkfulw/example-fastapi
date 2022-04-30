"""add last few columns to posts table

Revision ID: 8da157d9a990
Revises: cd4bf69b5f63
Create Date: 2022-04-24 20:40:12.615184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8da157d9a990"
down_revision = "cd4bf69b5f63"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
