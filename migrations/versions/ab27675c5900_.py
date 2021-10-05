"""empty message

Revision ID: ab27675c5900
Revises: dc00da42a3a2
Create Date: 2021-10-05 16:38:04.902148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab27675c5900'
down_revision = 'dc00da42a3a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pergunta',
    sa.Column('id_pergunta', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data_hora', sa.DateTime(), nullable=False),
    sa.Column('is_respondida', sa.Boolean(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('id_sala', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_sala'], ['sala.id_sala'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id_user'], ),
    sa.PrimaryKeyConstraint('id_pergunta')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pergunta')
    # ### end Alembic commands ###