#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect('database.db')


# In[2]:


from datetime import datetime

conn.execute("""CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                author TEXT,
                pages INTEGER,
                published INTEGER                
                )""")

values = ('Deep Learning', 
          'Ian Goodfellow et al.', 
          775, 
          datetime(2016, 11, 18).timestamp())

conn.execute("""INSERT INTO books VALUES (?, ?, ?, ?)""", values)


# In[3]:


r = conn.execute("""SELECT * FROM books""")
r.fetchall()


# In[4]:


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)
    
    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>"                .format(self.title, self.author, self.pages, self.published)


# In[11]:


from sqlalchemy import create_engine
import psycopg2
DATABASE_URI = 'postgresql+psycopg2://postgres:Utkarshsm@localhost:5432/books'


# In[12]:


engine = create_engine(DATABASE_URI)


# In[13]:



Base.metadata.create_all(engine)


# In[14]:


Base.metadata.drop_all(engine)


# In[15]:


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


# In[16]:


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


# In[17]:


s = Session()


# In[18]:


s.close()


# In[19]:


book = Book(
    title='Deep Learning',
    author='Ian Goodfellow',
    pages=775,
    published=datetime(2016, 11, 18)
)


# In[20]:


recreate_database()

s = Session()


# In[21]:


s.add(book)
s.commit()


# In[22]:


s.query(Book).first()


# In[25]:


s.close_all()
recreate_database()
s = Session()


# In[ ]:




