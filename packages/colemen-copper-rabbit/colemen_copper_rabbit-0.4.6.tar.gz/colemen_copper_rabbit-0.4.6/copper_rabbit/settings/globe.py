




from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine as _create_engine
from sqlalchemy import Engine
# from flask_sqlalchemy import SQLAlchemy
from flask import Response
from sqlalchemy.orm import sessionmaker as _sessionmaker
from copper_rabbit.settings import types as _t
from copper_rabbit.support.Result import Result

from flask import Flask

base = declarative_base()
db = None
session:Session = None
engine:Engine = None
app:Flask = None
_RESULT:_t._result_type = None
response:Response = Response()
'''The final response instance.'''
user = None


def result()->_t._result_type:
    if _RESULT is None:
        _RESULT = Result()
    return _RESULT


# session:Session = None


# from sqlalchemy.orm import DeclarativeBase


# class Base(DeclarativeBase):
#     pass