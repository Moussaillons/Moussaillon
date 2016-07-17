from flask import Flask, render_template
app = Flask(__name__)

app.config['SERVER_NAME'] = 'federation.dev'

@app.route('/', subdomain='<association_name>')
def website_home_route(association_name):
    return "Welcome to "+association_name+" website"

@app.route('/')
def root_route():
    return render_template('panel/text.html', title="Dashboard", content="Bienvenue!")

@app.route('/login')
def login_route():
    return render_template('panel/text.html', title="Login", content="not implemented yet")

@app.route('/posts/')
def posts_route():
    return render_template('panel/text.html', title="Posts", content="not implemented yet")

@app.route('/posts/new')
def new_post_route():
    return render_template('panel/text.html', title="New Post", content="not implemented yet")

@app.route('/posts/<string:post_name>')
def edit_post_route(post_name):
    return render_template('panel/text.html', title="Edit post: " + post_name, content="not implemented yet")

@app.route('/gallery/')
def gallery_route():
    return render_template('panel/text.html', title="Gallery", content="not implemented yet")

@app.route('/gallery/upload')
def upload_route():
    return render_template('panel/text.html', title="Upload items", content="not implemented yet")

@app.route('/calendar/')
def calendar_route():
    return render_template('panel/text.html', title="Events", content="not implemented yet")

@app.route('/calendar/new')
def new_event_route():
    return render_template('panel/text.html', title="New event", content="not implemented yet")

@app.route('/calendar/<string:event_name>')
def edit_event_route(event_name):
    return render_template('panel/text.html', title="Edit event: " + event_name, content="not implemented yet")

if __name__ == '__main__':
    app.run()
