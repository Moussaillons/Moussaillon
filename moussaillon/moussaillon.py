from flask import Flask, render_template
app = Flask(__name__)

app.config.from_pyfile('moussaillon_default_settings.cfg')
app.config.from_pyfile('server_config.cfg', silent=True)


@app.route('/')
@app.route('/', subdomain='<association_name>')
def website_home_route(association_name=""):
    return "Welcome to "+association_name+" website"


@app.route('/panel/')
@app.route('/panel/', subdomain='<association_name>')
def root_route(association_name=""):
    return render_template('panel/text.html',
                           title="Dashboard",
                           content="Bienvenue!")


@app.route('/panel/login')
@app.route('/panel/login', subdomain='<association_name>')
def login_route(association_name=""):
    return render_template('panel/text.html',
                           title="Login",
                           content="not implemented yet")


@app.route('/panel/posts/')
@app.route('/panel/posts/', subdomain='<association_name>')
def posts_route(association_name=""):
    return render_template('panel/text.html',
                           title="Posts",
                           content="not implemented yet")


@app.route('/panel/posts/new')
@app.route('/panel/posts/new', subdomain='<association_name>')
def new_post_route(association_name=""):
    return render_template('panel/text.html',
                           title="New Post",
                           content="not implemented yet")


@app.route('/panel/posts/<string:post_name>')
@app.route('/panel/posts/<string:post_name>', subdomain='<association_name>')
def edit_post_route(post_name, association_name=""):
    return render_template('panel/text.html',
                           title="Edit post: " + post_name,
                           content="not implemented yet")


@app.route('/panel/gallery/')
@app.route('/panel/gallery/', subdomain='<association_name>')
def gallery_route(association_name=""):
    return render_template('panel/text.html',
                           title="Gallery",
                           content="not implemented yet")


@app.route('/panel/gallery/upload')
@app.route('/panel/gallery/upload', subdomain='<association_name>')
def upload_route(association_name=""):
    return render_template('panel/text.html',
                           title="Upload items",
                           content="not implemented yet")


@app.route('/panel/calendar/')
@app.route('/panel/calendar/', subdomain='<association_name>')
def calendar_route(association_name=""):
    return render_template('panel/text.html',
                           title="Events",
                           content="not implemented yet")


@app.route('/panel/calendar/new')
@app.route('/panel/calendar/new', subdomain='<association_name>')
def new_event_route(association_name=""):
    return render_template('panel/text.html',
                           title="New event",
                           content="not implemented yet")


@app.route('/panel/calendar/<string:event_name>')
@app.route('/panel/calendar/<string:event_name>',
           subdomain='<association_name>')
def edit_event_route(event_name, association_name=""):
    return render_template('panel/text.html',
                           title="Edit event: " + event_name,
                           content="not implemented yet")


if __name__ == '__main__':
    app.run()
