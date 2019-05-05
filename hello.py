import findLinks
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'BEGINNING WORLD TAKEOVER'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # showing the username
    return 'user %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/search/<searchTxt>')
def search(searchTxt):
    print('finding links')
    output = findLinks.getTitle(searchTxt)
    return output
