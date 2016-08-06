"""
Defines routes of Moussaillon.

A CMS for associations' federations
:licence: aGLP
"""

from flask import Flask, render_template, g, session, redirect, url_for
app = Flask(__name__)

app.config.from_pyfile('moussaillon_default_settings.cfg')
app.config.from_pyfile('server_config.cfg', silent=True)


# Database functions
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DB_URI'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# Session functions
def is_valid_session():
    if not session.get('session_id'):
        return False
    session_id = session.get('session_id')
    cursor = get_db().cursor()
    values = (session_id, )
    cursor.execute('SELECT * FROM sessions WHERE id=?', values)
    result = cursor.fetchone()
    if result is None:
        return False
    elif result['creation']+(SESSION_DURATION) < localtime():
        return False
    else:
        return True


# Routes
@app.route('/')
@app.route('/', subdomain='<association_name>')
def website_home_route(association_name=""):
    return "Welcome to "+association_name+" website"


@app.route('/panel/')
@app.route('/panel/', subdomain='<association_name>')
def root_route(association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    else:
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
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Posts",
                           content="not implemented yet")


@app.route('/panel/posts/new')
@app.route('/panel/posts/new', subdomain='<association_name>')
def new_post_route(association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="New Post",
                           content="not implemented yet")


@app.route('/panel/posts/<string:post_name>')
@app.route('/panel/posts/<string:post_name>', subdomain='<association_name>')
def edit_post_route(post_name, association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Edit post: " + post_name,
                           content="not implemented yet")


@app.route('/panel/gallery/')
@app.route('/panel/gallery/', subdomain='<association_name>')
def gallery_route(association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Gallery",
                           content="not implemented yet")


@app.route('/panel/gallery/upload')
@app.route('/panel/gallery/upload', subdomain='<association_name>')
def upload_route(association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Upload items",
                           content="not implemented yet")


@app.route('/panel/calendar/')
@app.route('/panel/calendar/', subdomain='<association_name>')
def calendar_route(association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Events",
                           content="not implemented yet")


@app.route('/panel/calendar/new')
@app.route('/panel/calendar/new', subdomain='<association_name>')
def new_event_route(association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="New event",
                           content="not implemented yet")


@app.route('/panel/calendar/<string:event_name>')
@app.route('/panel/calendar/<string:event_name>',
           subdomain='<association_name>')
def edit_event_route(event_name, association_name=""):
    if not is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Edit event: " + event_name,
                           content="not implemented yet")


if __name__ == '__main__':
    app.run()
