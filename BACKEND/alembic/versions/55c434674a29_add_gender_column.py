"""add gender column

Revision ID: 55c434674a29
Revises: c1eceb8f40c8
Create Date: 2025-10-27 15:02:06.709562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55c434674a29'
down_revision: Union[str, Sequence[str], None] = 'c1eceb8f40c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        ALTER TABLE users
        ADD COLUMN gender ENUM('male', 'female') DEFAULT 'male';
            """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE users
        DROP COLUMN userType
               """)
    pass
