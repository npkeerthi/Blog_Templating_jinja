from flask import Flask, render_template
import requests

posts=requests.get(url="https://api.npoint.io/1d52267d24c52548af31").json()
postobjects=[]


from post import Post
for p in posts:
    postobj= Post(p["id"],p["title"],p["subtitle"],p["body"])
    postobjects.append(postobj)



app = Flask(__name__)

@app.route('/')
def getposts():
    return render_template("index.html",allposts=postobjects)

@app.route('/post/<int:id>')
def openpost(id):
    tobeopened = None
    for thispost in postobjects:
        if thispost.id == id:
            tobeopened = thispost
    return render_template("post.html" , POST=tobeopened)


if __name__ == "__main__":
    app.run(debug=True)
