from typing import Optional

from sqlalchemy.engine import Engine, Result
from sqlalchemy import text

from preql.core.models import Environment, ProcessedQuery
from preql.dialect.base import BaseDialect
from preql.dialect.enums import Dialects
from preql.parser import parse_text
from typing import List
from preql.constants import logger


class Executor(object):
    def __init__(
        self,
        dialect: Dialects,
        engine: Engine,
        environment: Optional[Environment] = None,
    ):
        self.dialect = dialect
        self.engine = engine
        self.environment = environment or Environment()
        self.generator: BaseDialect
        self.logger = logger
        if self.dialect == Dialects.BIGQUERY:
            from preql.dialect.bigquery import BigqueryDialect

            self.generator = BigqueryDialect()
        elif self.dialect == Dialects.SQL_SERVER:
            from preql.dialect.sql_server import SqlServerDialect

            self.generator = SqlServerDialect()
        elif self.dialect == Dialects.DUCK_DB:
            from preql.dialect.duckdb import DuckDBDialect

            self.generator = DuckDBDialect()
        else:
            raise ValueError(f"Unsupported dialect {self.dialect}")

    def execute_query(self, query: ProcessedQuery) -> Result:

        sql = self.generator.compile_statement(query)
        connection = self.engine.connect()
        output = connection.execute(text(sql))
        return output

    def execute_text(self, command: str) -> List[Result]:
        _, parsed = parse_text(command, self.environment)
        sql = self.generator.generate_queries(self.environment, parsed)
        output = []
        connection = self.engine.connect()
        for statement in sql:
            compiled_sql = self.generator.compile_statement(statement)
            logger.debug(compiled_sql)
            output.append(connection.execute(text(compiled_sql)))
        return output
