from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'))
def main():
  if request.method == 'POST':
    post = request.form["post"]
    blog = request.form["blog"]
    if post != None and blog != None:
      #insert post into blog db under blog name
      redirect(url_for("blog", blog_name = blog))
    return render_template("main.html")

@app.route("/blog/<blog_name>", methods = ["GET", "POST"])
def blog(blog_name):
  if request.method == "POST":
    post_ID = request.form["comment"]
    redirect(url_for("post_page", postID = post_ID))
  #return render_template("blog.html")
  return render_template("main.html") #for now, goes back to main page
#wll show posts of blog newest to oldest

@app.route("/<postID>")
def post_page(postID = None):
  #return render_template("post.html", name = post_name, content = post_content)
  #from postID, we access the database to extract post_name and post_content
  return render_template("main.html")#for now, just return main page
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=1639)
    app.run()
