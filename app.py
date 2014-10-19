from flask import Flask, render_template, request

app = Flask(__name__)

app.route("/")
def main():
  return render_template("main.html")
  
app.route("/<postID>")
def post_page(postID = None):
  #return render_template("post.html", name = post_name, content = post_content)
  #from postID, we access the database to extract post_name and post_content
