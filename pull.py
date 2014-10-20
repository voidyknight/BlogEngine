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
def addPost(blog, post):
    q ="INSERT TO posts VALUES("+blog+","+post+");"
    result = c.execute(q)
    
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
