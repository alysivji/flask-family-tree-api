"""=create spouse table

Revision ID: ac04e6c59b74
Revises: 96771670b47d
Create Date: 2019-02-16 16:34:54.906106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac04e6c59b74'
down_revision = '96771670b47d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spouse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('spouse_person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['spouse_person_id'], ['person.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spouse')
    # ### end Alembic commands ###
