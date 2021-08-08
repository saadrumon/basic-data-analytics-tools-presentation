from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql.functions import user
import os

path = os.path.dirname(__file__)
engine = create_engine(f'sqlite:///{os.path.join(path, "database.db")}')
meta = MetaData()

posts = Table(
   'posts', meta, 
   Column('id', Integer, primary_key = True, autoincrement=True), 
   Column('userId', Integer), 
   Column('title', String),
   Column('body', String), 
)

meta.create_all(engine)

conn = engine.connect()

result = conn.execute(posts.insert(), [
    { 'userId': 0, 'title': 'title 0', 'body': 'body 0' },
    { 'userId': 1, 'title': 'title 1', 'body': 'body 1' },
])

result = conn.execute(posts.select())
for row in result:
    print(row)
