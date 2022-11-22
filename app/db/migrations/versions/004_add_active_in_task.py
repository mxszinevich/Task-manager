"""004_add_active_in_task

Revision ID: b9cd3b627099
Revises: 2709611cea32
Create Date: 2022-11-21 23:04:32.031216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b9cd3b627099"
down_revision = "2709611cea32"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("tasks", sa.Column("active", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tasks", "active")
    # ### end Alembic commands ###
