from flask import session
from moussaillon import app, database
import datetime
import time
import os
import base64
from werkzeug.security import generate_password_hash, \
     check_password_hash


def create_session(email, password):
    cursor = database.get_db().cursor()
    values = (email, )
    cursor.execute('SELECT * FROM members WHERE mail=?', values)
    result = cursor.fetchone()
    if result is None:
        return False
    elif check_password_hash(result['password'], password):
        # generate a new key
        key = base64.b64encode(os.urandom(32))
        values = (key, )
        cursor.execute('SELECT member FROM sessions WHERE key=?', values)
        while cursor.fetchone() is not None:
            key = base64.b64encode(os.urandom(32))
            values = (key, )
            cursor.execute('SELECT user FROM sessions WHERE key=?', values)

        # insert it
        values = (key, 'now', result['id'], )
        cursor.execute('INSERT into sessions(key, last_ping, member)' +
                       'VALUES (?, datetime(?), ?)', values)
        database.get_db().commit()
        session['session_key'] = key
        print("session started: ", key)
        return True
    else:
        return False


def is_valid_session():
    if not session.get('session_key'):
        return False
    session_id = session.get('session_key')
    print("testing session: ", session_id)
    cursor = database.get_db().cursor()
    values = (session_id, )
    cursor.execute('SELECT * FROM sessions WHERE key=?', values)
    result = cursor.fetchone()
    if result is None:
        session.pop('session_key')
        return False
    else:
        now = datetime.datetime.utcnow().timestamp()
        last_ping = datetime.datetime.strptime(result['last_ping'],
                                               "%Y-%m-%d %H:%M:%S").timestamp()
        max_timeout = app.config['SESSION_DURATION']
        if now - last_ping > max_timeout:
            session.pop('session_key')
            return False
        else:
            values = ('now', session_id)
            cursor.execute('UPDATE sessions SET last_ping = datetime(?)' +
                           'WHERE key=?', values)
            database.get_db().commit()
            print("updated session: ", session['session_key'])
            return True


def logout():
    if not session.get('session_key'):
        return False
    session_id = session.get('session_key')
    print("testing session: ", session_id)
    cursor = database.get_db().cursor()
    values = (session_id, )
    cursor.execute('SELECT * FROM sessions WHERE key=?', values)
    result = cursor.fetchone()
    if result is None:
        session.pop('session_key')
        return False
    else:
        values = (session_id, )
        cursor.execute('DELETE FROM sessions WHERE key=?', values)
        database.get_db().commit()
        session.pop('session_key')
        return True


def update_timeout():
    print("not yet implemented")
