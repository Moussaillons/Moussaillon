from flask import session


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
