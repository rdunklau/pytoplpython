from pytoplpython import PostgresLoader
from sqlalchemy import create_engine

engine = create_engine('postgresql://python@localhost/')

loader = PostgresLoader(engine)

testmodule = loader.load_module('testmodule')

print(engine.execute(testmodule.test('grou')).fetchall())

print(engine.execute(testmodule.pyconcat('col1', 'col2')).fetchall())
