"""alter user table

Revision ID: c746e545645e
Revises: 
Create Date: 2025-10-23 11:21:18.121395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c746e545645e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE users
        ADD COLUMN userType VARCHAR(255) DEFAULT 'student' ENUM('student' 'admin')
               """)
    pass


def downgrade() -> None:
    op.execute("""
        ALTER TABLE users
        DROP COLUMN userType
               """)
    pass
