"""
Defines routes of Moussaillon.

A CMS for associations' federations
:licence: aGPL
"""

from flask import Flask, render_template, redirect, url_for, request
import header
import session
import database
import template
app = header.app


# Database functions
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    database.init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_connections(error):
    database.close_db(error)


# Routes
@app.route('/')
@app.route('/', subdomain='<association_name>')
def website_home_route(association_name=""):
    site = template.get_site_config(association_name)
    posts = template.get_posts(site['id'])
    return render_template('posts.html', site=site, posts=posts)


@app.route('/panel/login', methods=['GET', 'POST'])
@app.route('/panel/login', subdomain='<association_name>',
           methods=['GET', 'POST'])
def login_route(association_name=""):
    if session.is_valid_session():
        return redirect(url_for('dashboard_route'))
    if request.method == 'POST':
        created_session = session.create_session(request.form['email'],
                                                 request.form['password'])
        print(created_session)
        if created_session is True:
            return redirect(url_for('dashboard_route'))
        print("no session created")
    return render_template('panel/login.html')


@app.route('/panel/logout')
@app.route('/panel/logout', subdomain='<association_name>')
def logout_route(association_name=""):
    if session.is_valid_session():
        session.logout()
    return redirect(url_for('website_home_route'))


@app.route('/panel/login', methods=['GET', 'POST'])
@app.route('/panel/login', subdomain='<association_name>',
           methods=['GET', 'POST'])
def login_route(association_name=""):
    if session.is_valid_session():
        return redirect(url_for('dashboard_route'))
    if request.method == 'POST':
        created_session = session.create_session(request.form['email'],
                                                 request.form['password'])
        print(created_session)
        if created_session is True:
            return redirect(url_for('dashboard_route'))
        print("no session created")
    return render_template('panel/login.html')


@app.route('/panel/logout')
@app.route('/panel/logout', subdomain='<association_name>')
def logout_route(association_name=""):
    if session.is_valid_session():
        session.logout()
    return redirect(url_for('website_home_route'))


@app.route('/panel/')
@app.route('/panel/', subdomain='<association_name>')
def dashboard_route(association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    else:
        return render_template('panel/text.html',
                               title="Dashboard",
                               content="Bienvenue!")


@app.route('/panel/posts/')
@app.route('/panel/posts/', subdomain='<association_name>')
def posts_route(association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Posts",
                           content="not implemented yet")


@app.route('/panel/posts/new')
@app.route('/panel/posts/new', subdomain='<association_name>')
def new_post_route(association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="New Post",
                           content="not implemented yet")


@app.route('/panel/posts/<string:post_name>')
@app.route('/panel/posts/<string:post_name>', subdomain='<association_name>')
def edit_post_route(post_name, association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Edit post: " + post_name,
                           content="not implemented yet")


@app.route('/panel/gallery/')
@app.route('/panel/gallery/', subdomain='<association_name>')
def gallery_route(association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Gallery",
                           content="not implemented yet")


@app.route('/panel/gallery/upload')
@app.route('/panel/gallery/upload', subdomain='<association_name>')
def upload_route(association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Upload items",
                           content="not implemented yet")


@app.route('/panel/calendar/')
@app.route('/panel/calendar/', subdomain='<association_name>')
def calendar_route(association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Events",
                           content="not implemented yet")


@app.route('/panel/calendar/new')
@app.route('/panel/calendar/new', subdomain='<association_name>')
def new_event_route(association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="New event",
                           content="not implemented yet")


@app.route('/panel/calendar/<string:event_name>')
@app.route('/panel/calendar/<string:event_name>',
           subdomain='<association_name>')
def edit_event_route(event_name, association_name=""):
    if not session.is_valid_session():
        return redirect(url_for('login_route'))
    return render_template('panel/text.html',
                           title="Edit event: " + event_name,
                           content="not implemented yet")


if __name__ == '__main__':
    app.run()
