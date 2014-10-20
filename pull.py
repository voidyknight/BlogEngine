import sqlite3

conn = sqlite3.connect("blogs.db")
c = conn.cursor()

def pullBlog(blogName):
    query="select post from blogs posts where name == "+blogName;
    results = c.execute(q)
    posts=[]
    for post in results:
        posts.append(post[0])
    return posts

    
def addPost(blog, post):
    q ="INSERT TO posts VALUES("+blog+","+post+");"
    results = c.execute(q)
    c.commit()
def getBlogs():
    q ="""
    select name from blogs;
    """
    
    result = c.execute(q)
    print result
    blogs=[]
    for blog in results:
        blogs.append(blog)
        

    return blogs
