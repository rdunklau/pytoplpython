from pytoplpython import postgresql_function
from sqlalchemy.types import Unicode, Integer

@postgresql_function
def test(test: Unicode) -> Unicode:
    return 'test function'

@postgresql_function
def pyconcat(col1: Unicode, col2: Unicode) -> Unicode:
    return col1 + col2

@postgresql_function
def pygreatest(col1: Integer, col2: Integer) -> Integer:
    return max(col1, col2)

@postgresql_function
def nullifying_trigger() -> TRIGGER:
    TD['new']['test2'] = 'triggered by me'
    return 'MODIFY'
