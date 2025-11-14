"""alter users table

Revision ID: 12579648ec18
Revises: 
Create Date: 2025-10-27 12:45:13.934251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12579648ec18'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        ALTER TABLE users
        ADD COLUMN gender VARCHAR(50) DEFAULT 'male' ENUM("male" "female")
               """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE users
        Drop COLUMN gender
               """)
    pass
