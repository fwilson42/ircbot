"""kick logging change

Revision ID: 3614b38ddf9
Revises: ef7ccebeff
Create Date: 2015-04-23 15:55:07.747669

"""

# revision identifiers, used by Alembic.
revision = '3614b38ddf9'
down_revision = 'ef7ccebeff'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    log = sa.table('log', sa.column('type', sa.String), sa.column('msg', sa.String))
    rows = op.get_bind().execute(log.select().where(log.c.type == 'kick').where(log.c.msg.like('%,%'))).fetchall()
    values = [{'old_msg': x.msg, 'msg': x.msg.replace(',', ' ', 1)} for x in rows]
    op.get_bind().execute(log.update().where(log.c.msg == sa.bindparam('old_msg')).values(msg=sa.bindparam('msg')), values)


def downgrade():
    # FIXME: this adds extraneous commas
    return
    log = sa.table('log', sa.column('type', sa.String), sa.column('msg', sa.String))
    rows = op.get_bind().execute(log.select().where(log.c.type == 'kick')).fetchall()
    values = [{'old_msg': x.msg, 'msg': x.msg.replace(' ', ',', 1)} for x in rows]
    op.get_bind().execute(log.update().where(log.c.msg == sa.bindparam('old_msg')).values(msg=sa.bindparam('msg')), values)