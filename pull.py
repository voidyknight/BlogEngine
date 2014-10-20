import sqlite3

conn = sqlite3.connect("blogs.db")
c = conn.cursor()

def pullBlog(blogName):
    #bName = open('insert file here', 'r')
    '''
    bName = bName.readlines()
    int counter = 0;
    while (counter < bName.len()):
        if (bName[counter] ==  blogName):


        counter = bName.len()
    '''
    query="select post from blogs posts where name == blog";
    results = c.execute(q)
    
def addPost(blog, post):
    q ="INSERT TO posts VALUES("+blog+","+post+");"
    results = c.execute(q)
    posts=[]
    for post in results:
        posts.append(post[0])
    return posts
    
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
