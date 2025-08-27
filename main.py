from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from flask import Flask, request, redirect

engine = create_engine('sqlite:///dados.db')
Base = declarative_base()
_Sessao = sessionmaker(engine)

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), unique=True)

Base.metadata.create_all(engine)

app = Flask(__name__)

from views import *

if __name__ == '__main__':
    app.run(debug=True)