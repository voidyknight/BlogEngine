import sqlite3

conn = sqlite3.connect("blogs.db")

q = "create table blogs(name text)"
c = conn.cursor()
c.execute(q)

q="""
create table posts (blog text, post text)
"""
c.execute(q);

q="""
create table comments (blog integer, user text, comment text)
"""
c.execute(q);
conn.commit();
