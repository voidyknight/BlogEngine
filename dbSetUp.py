import sqlite3
conn = sqlite3.connect("blogs.db")
c = conn.cursor()

q = "create table if not exists blogs(name text UNIQUE)"
c = conn.cursor()
c.execute(q)

q="""
create table if not exists posts (blog text, post text)
"""
c.execute(q);

q="""
create table if not exists comments (post integer, user text, comment text)
"""

c.execute(q);
conn.commit();
conn.close();
