"""alter users table

Revision ID: c1eceb8f40c8
Revises: 
Create Date: 2025-10-27 14:48:43.088869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1eceb8f40c8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        ALTER TABLE users
        ADD COLUMN userType ENUM('student', 'admin') DEFAULT 'student';
            """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE users
        DROP COLUMN userType
               """)
    pass
