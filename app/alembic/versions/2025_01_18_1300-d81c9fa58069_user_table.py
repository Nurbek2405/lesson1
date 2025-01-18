"""user_table

Revision ID: d81c9fa58069
Revises: 
Create Date: 2025-01-18 13:00:46.181866

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "d81c9fa58069"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("roles")
    op.add_column(
        "users",
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.add_column(
        "users",
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )


def downgrade() -> None:
    op.drop_column("users", "updated_at")
    op.drop_column("users", "created_at")
    op.create_table(
        "roles",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False,),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=False,),
        sa.Column("created_at",postgresql.TIMESTAMP(timezone=True),autoincrement=False,nullable=False,),
        sa.Column("updated_at",postgresql.TIMESTAMP(timezone=True),autoincrement=False,nullable=False,),
        sa.PrimaryKeyConstraint("id", name="roles_pkey"),
        sa.UniqueConstraint("title", name="roles_title_key"),
    )
