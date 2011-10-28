from importlib.abc import InspectLoader
import imp
import sys
import ast
from .unparse import Unparser
from io import StringIO
from tempfile import NamedTemporaryFile

def postgresql_function(function):
    """Decorator used to mark a function as executable in postgresql"""
    pass

class PostgresLoader(InspectLoader):

    def __init__(self, engine):
        self.engine = engine

    def get_code(self, path):
        pass

    def load_module(self, fullname, path=None):
        newsource, filename, stuff = self.get_source(fullname)
        temp_file = NamedTemporaryFile(mode="w")
        temp_file.write('from sqlalchemy.sql import func\n')
        temp_file.write(newsource.read())
        temp_file.seek(0)
        module = imp.load_module(fullname, temp_file, filename, stuff)
        return module

    def is_package(self, fullname):
        pass

    def get_source(self, fullname):
        subname = fullname.split('.')[-1]
        file, filename, stuff = imp.find_module(subname, sys.path)
        source = file.read()
        tree = ast.parse(source)
        newsource = StringIO()
        Unparser(tree, self.engine, newsource)
        newsource.seek(0)
        newsource.seek(0)
        return newsource, filename, stuff
