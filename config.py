from sqlalchemy.ext.declarative import declarative_base

REPO_PATH = '../edx-platform'

DB_PATH = 'edx-platform.sqlite'
DB_TYPE = 'sqlite:///'
DB_URL = DB_TYPE + DB_PATH

BASE = declarative_base()

RESET_DB = True # if True, deletes the DB every time you run create_database