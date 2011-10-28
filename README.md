Python to PL/Python
===================

This is a quick'n'dirty proof of concept using python 3 type annotations and
import Loaders to automatically convert python code to pl/python functions.


Usage
=====

First, define a module that will contains function you want to test
('mymodule.py')

Note how we write function annotations to get the args and return types.

```python
from pytoplpython import postgresql_function
from sqlalchemy.types import Integer

@postgresql_function
def greatest(col1: Integer, col2: Integer) -> Integer:
    return max(col1, col2)
```


```python
from pytoplpython import PostgresLoader
from sqlalchemy import create_engine

# Create the sqlalchemy engine
# Note: the user must be a superuser to use pl/python and the 
# pl/pythonu language must be installed on the target dabase
engine = create_engine('postgresql://python@localhost/')

# Create the loader, and load the module containing the functions
# This will create the associated pl/python functions, and replace them 
# with sqlalchemy functions, which can operate on columns
loader = PostgresLoader(engine)
mymodule = loader.load_module('mymodule')

engine.execute(testmodule.greatest(1, 3)).fetchone()
```

See the [test/basetest.py](http://github.com/rdunklau/pytoplpython/tree/master/test/basetest.py) and [test/testmodule.py](http://github.com/rdunklau/pytoplpython/tree/master/test/testmodule.py) files for additional information
