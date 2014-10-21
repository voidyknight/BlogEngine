from flask import Flask, render_template, request, redirect, url_for 
import sqlite3,pull

app = Flask(__name__)
conn = sqlite3.connect("blogs.db", check_same_thread=False)
c = conn.cursor()

def getBlogs():
    q ="""
    select name from  blogs
    """
    
    results = c.execute(q)
    print results
    blogs=[]
    for blog in results:
        blogs.append(blog[0])
        

    return blogs

@app.route("/", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        post = request.form["post"]
        blog = request.form["blog"]
        if post != None and blog != None:
            print "INSERT INTO posts VALUES ('"+blog+"', '"+post+"')"
            c.execute("INSERT INTO posts VALUES ('"+blog+"', '"+post+"')")
            try:
                c.execute("INSERT INTO blogs VALUES ('"+blog+"')")
            except:
                pass
            conn.commit()
            return redirect(url_for("blog", blog_name = blog))
    return render_template("main.html", blogs=getBlogs())

@app.route("/blog/<blog_name>", methods = ["GET", "POST"])
def blog(blog_name):
    if request.method == "POST":
        post_ID = request.form["comment"]
        return redirect(url_for("post_page", postID = post_ID, blogname = blog_name))
    return render_template("blog.html",
                           posts = pull.pullBlog(blog_name), title = blog_name)
#wll show posts of blog newest to oldest

@app.route("/blog/<blogname>/post/<postID>",  methods = ["GET", "POST"])
def post_page(blogname, postID):
    post = pull.getPost(postID)
    new_commenter = request.args.get("user",None)
    new_comment = request.args.get("comment",None)
    if new_commenter != None and new_comment != None:
        #adding a new comment
        pull.addComment(postID,new_commenter,new_comment)
    all_comments = pull.getComments(postID) #all the comments for the post
    return render_template("post.html", title = post[0], post = post[1], comments = all_comments)



  
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=1639)
    app.run()
