from flask import Flask
app = Flask(__name__)

app.config['SERVER_NAME'] = 'federation.dev:5000'

@app.route('/', subdomain='<association_name>')
def website_home_route(association_name):
    return "Welcome to "+association_name+" website"

@app.route('/')
def root_route():
    return "Root"

@app.route('/login')
def login_route():
    return "Login"

@app.route('/posts/')
def posts_route():
    return "Posts"

@app.route('/posts/new')
def new_post_route():
    return "New post"

@app.route('/posts/<string:post_name>')
def edit_post_route(post_name):
    return "Edit post: " + post_name

@app.route('/gallery/')
def gallery_route():
    return "Gallery"

@app.route('/gallery/upload')
def upload_route():
    return "Upload items"

@app.route('/calendar/')
def calendar_route():
    return "Events"

@app.route('/calendar/new')
def new_event_route():
    return "New event"

@app.route('/calendar/<string:event_name>')
def edit_event_route(event_name):
    return "Edit event: " + event_name

if __name__ == '__main__':
    app.run()
