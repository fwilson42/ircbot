# Stubs for alembic.ddl.sqlite (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .impl import DefaultImpl
from typing import Any


class SQLiteImpl(DefaultImpl):
    __dialect__: str = ...
    transactional_ddl: bool = ...

    def requires_recreate_in_batch(self, batch_op: Any):
        ...

    def add_constraint(self, const: Any) -> None:
        ...

    def drop_constraint(self, const: Any) -> None:
        ...

    def compare_server_default(self, inspector_column: Any, metadata_column: Any, rendered_metadata_default: Any, rendered_inspector_default: Any):
        ...

    def autogen_column_reflect(self, inspector: Any, table: Any, column_info: Any) -> None:
        ...

    def render_ddl_sql_expr(self, expr: Any, is_server_default: bool = ..., **kw: Any):
        ...