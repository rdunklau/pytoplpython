from pytoplpython import PostgresLoader
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData, Table, Column
from sqlalchemy.types import Unicode

engine = create_engine('postgresql://python@localhost/')

loader = PostgresLoader(engine)

testmodule = loader.load_module('testmodule')

metadata = MetaData(bind=engine)

table = Table('testtable', metadata,
        Column('test', Unicode),
        Column('test2', Unicode))

table.create(checkfirst=True)

for i in range(20):
    table.insert({'test': 'test%d' % i, 'test2': 'test%d' %i}).execute()

print(engine.execute(testmodule.pyconcat(table.c.test, table.c.test2)).fetchall())



print(engine.execute(testmodule.pygreatest(1, 3)).fetchone())
