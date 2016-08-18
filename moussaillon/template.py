import header
import database


def get_site_config(subdomain=''):
    site = {}
    cursor = database.get_db().cursor()

    # ask db
    values = (subdomain, )
    cursor.execute('SELECT * FROM sites WHERE uri=?', values)
    result = cursor.fetchone()

    # if is not a subdomain, tell parent
    if result is False:
        return False

    # show it for debug
    for key in result.keys():
        print(key, ": ", result[key])

    # set name
    site['name'] = result['name']

    # set id
    site['id'] = result['id']

    return site


def get_posts(subdomain_id=1):
    cursor = database.get_db().cursor()

    # ask db
    values = (subdomain_id, )
    cursor.execute('SELECT * FROM posts WHERE site=?', values)
    posts = cursor.fetchall()

    return posts
