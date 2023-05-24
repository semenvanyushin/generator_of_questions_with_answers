"""Column answer type str

Revision ID: 0e34646aef9f
Revises: 5bc692e58653
Create Date: 2023-05-24 15:49:51.636029

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0e34646aef9f'
down_revision = '5bc692e58653'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_question_id', table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('answer', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='question_pkey')
    )
    op.create_index('ix_question_id', 'question', ['id'], unique=False)
    # ### end Alembic commands ###
