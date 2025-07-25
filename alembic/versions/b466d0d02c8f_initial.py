"""initial

Revision ID: b466d0d02c8f
Revises: 
Create Date: 2025-07-18 17:35:42.298470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b466d0d02c8f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('name_ka', sa.String(length=255), nullable=False),
    sa.Column('name_en', sa.String(length=255), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=False),
    sa.Column('icon', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('brand', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('size', sa.String(length=255), nullable=True),
    sa.Column('keywords', sa.Text(), nullable=True),
    sa.Column('upc', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('stores',
    sa.Column('store_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('latitude', sa.DECIMAL(precision=9, scale=6), nullable=True),
    sa.Column('longitude', sa.DECIMAL(precision=9, scale=6), nullable=True),
    sa.Column('chain_id', sa.Integer(), nullable=True),
    sa.Column('api_source', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('location_permission_granted', sa.Boolean(), nullable=True),
    sa.Column('notification_preferences', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('favorites',
    sa.Column('favorite_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.Column('notify_on_sale', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('favorite_id')
    )
    op.create_table('inventory',
    sa.Column('inventory_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('last_restocked', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.store_id'], ),
    sa.PrimaryKeyConstraint('inventory_id')
    )
    op.create_table('notifications',
    sa.Column('notification_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('extra_metadata', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.store_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('notification_id')
    )
    op.create_table('preferences',
    sa.Column('preference_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('dietary_filters', sa.String(length=255), nullable=True),
    sa.Column('favorite_stores', sa.Text(), nullable=True),
    sa.Column('saved_searches', sa.Text(), nullable=True),
    sa.Column('route_suggestions', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('preference_id')
    )
    op.create_table('price_history',
    sa.Column('history_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('was_on_sale', sa.Boolean(), nullable=True),
    sa.Column('sale_price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('recorded_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.store_id'], ),
    sa.PrimaryKeyConstraint('history_id')
    )
    op.create_table('prices',
    sa.Column('price_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('sale_price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('is_on_sale', sa.Boolean(), nullable=True),
    sa.Column('sale_start', sa.DateTime(), nullable=True),
    sa.Column('sale_end', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.store_id'], ),
    sa.PrimaryKeyConstraint('price_id')
    )
    op.create_table('sale_alerts',
    sa.Column('alert_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('notify_on_sale', sa.Boolean(), nullable=True),
    sa.Column('notify_if_already_on_sale', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_notified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('alert_id')
    )
    op.create_table('search_history',
    sa.Column('search_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('query', sa.Text(), nullable=True),
    sa.Column('searched_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('search_id')
    )
    op.create_table('sessions',
    sa.Column('session_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('is_guest', sa.Boolean(), nullable=True),
    sa.Column('is_first_time', sa.Boolean(), nullable=True),
    sa.Column('started_at', sa.DateTime(), nullable=True),
    sa.Column('last_active', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_table('shopping_lists',
    sa.Column('list_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('list_id')
    )
    op.create_table('smart_matching',
    sa.Column('match_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('input_query', sa.String(length=255), nullable=True),
    sa.Column('matched_product_id', sa.Integer(), nullable=True),
    sa.Column('confidence_score', sa.Float(), nullable=True),
    sa.Column('synonym_used', sa.String(length=255), nullable=True),
    sa.Column('variation_type', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['matched_product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('match_id')
    )
    op.create_table('shopping_list_items',
    sa.Column('item_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('added_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['list_id'], ['shopping_lists.list_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping_list_items')
    op.drop_table('smart_matching')
    op.drop_table('shopping_lists')
    op.drop_table('sessions')
    op.drop_table('search_history')
    op.drop_table('sale_alerts')
    op.drop_table('prices')
    op.drop_table('price_history')
    op.drop_table('preferences')
    op.drop_table('notifications')
    op.drop_table('inventory')
    op.drop_table('favorites')
    op.drop_table('users')
    op.drop_table('stores')
    op.drop_table('products')
    op.drop_table('categories')
    # ### end Alembic commands ###
