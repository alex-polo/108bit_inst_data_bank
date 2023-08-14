"""create database

Revision ID: 58c0beae2977
Revises: 
Create Date: 2023-08-14 12:19:46.911268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58c0beae2977'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system_name', sa.String(length=255), nullable=False),
    sa.Column('site_name', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('vendor_tag', sa.String(length=255), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=False),
    sa.Column('updated_on', sa.DateTime(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('site_name'),
    sa.UniqueConstraint('system_name')
    )
    op.create_table('field_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('site_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['site_id'], ['sites.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('field_tags')
    op.drop_table('sites')
    op.drop_table('sections')
    op.drop_table('products')
    op.drop_table('document')
    # ### end Alembic commands ###