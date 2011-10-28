from pytoplpython import postgresql_function
from sqlalchemy.types import Unicode

@postgresql_function
def test(test: Unicode) -> Unicode:
    return 'test function'

@postgresql_function
def pyconcat(col1: Unicode, col2: Unicode) -> Unicode:
    return col1 + col2

