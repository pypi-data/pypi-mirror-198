from pytest import fixture, mark
from paddl import parse, Table, ColType


class TestMySQL:
    @fixture
    def ddl(self):
        return open('data/ddls/overdraft.sql').read()

    def test_overdraft(self, ddl):
        schema = parse(ddl)
        tables = schema.tables
        account = tables[0]
        columns = account.columns
        id_col = columns[0]
        assert isinstance(tables[0], Table)
        assert account.name == 'account'
        assert id_col.name == 'id'
        assert id_col.type == ColType.CHAR

        assert columns[3].name == 'status'
        assert columns[3].type == ColType.ENUM

        assert columns[4].name == 'created'
        assert columns[4].type == ColType.DATETIME

        assert columns[5].name == 'updated'
        assert columns[5].type == ColType.DATETIME

        assert columns[6].name == 'deleted'
        assert columns[6].type == ColType.DATETIME
        assert len(account.columns) == 7

    def test_constraints(self, ddl):
        schema = parse(ddl)
        table = schema.tables[1]
        constraint = table.constraints[3]

        assert len(table.constraints) == 5
        assert constraint.symbol == 'adjustment_adjustment_source_id_foreign'
        assert constraint.key[0] == 'adjustment_source_id'
        assert constraint.ref_table == 'adjustment_source'
        assert constraint.ref_columns[0] == 'id'

    def test_table_count(self, ddl):
        schema = parse(ddl)
        table = schema.tables[0]
        assert len(schema.tables) == 9
        # assert len(schema.tables) == 36
