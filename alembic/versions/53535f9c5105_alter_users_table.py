"""alter users table

Revision ID: 53535f9c5105
Revises: d43b613d5d68
Create Date: 2025-10-27 11:37:16.114706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53535f9c5105'
down_revision: Union[str, Sequence[str], None] = 'd43b613d5d68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE users
        ADD COLUMN gender VARCHAR(50) DEFAULT 'male' ENUM("male" "female")
               """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
