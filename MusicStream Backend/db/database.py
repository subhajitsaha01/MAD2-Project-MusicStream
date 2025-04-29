#   establishing the database connection with the help of flask sql alchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

engine = None
base = declarative_base()
db = SQLAlchemy()