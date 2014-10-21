import sqlite3

conn = sqlite3.connect("blogs.db", check_same_thread=False)
c = conn.cursor()

def pullBlog(blogName):
    query="select posts.post,posts.rowid from blogs,posts where posts.blog == '"+blogName+"';"
    print query
    results = c.execute(query)
    print results
    posts=[]
    for post in results:
        print post
        if post not in posts:
            posts.append(post)
    print posts
    return posts

    
def addPost(blog, post):
    q ="INSERT TO posts VALUES("+blog+","+post+");"
    results = c.execute(q)
    c.commit()

def getPost(id):
    query="select posts.* from blogs,posts where posts.rowid=="+id+";"
    results= c.execute(query)
    for result in results:
        return result;
    
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
