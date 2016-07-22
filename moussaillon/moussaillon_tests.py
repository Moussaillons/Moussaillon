import os
import moussaillon
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        moussaillon.app.config['SERVER_NAME'] = 'localhost:5000'
        self.app = moussaillon.app.test_client()

    def tearDown(self):
        pass

    def test_homepage(self):
        req = self.app.get('/')
        assert b'Dashboard' in req.data

    def test_loginpage(self):
        req = self.app.get('/login')
        assert b'Login' in req.data

    def test_posts(self):
        req = self.app.get('/posts/')
        print req
        assert b'Posts' in req.data

    def test_posts_new(self):
        req = self.app.get('/posts/new')
        assert b'New Post' in req.data

    def test_edit_post(self):
        req = self.app.get('/posts/foo')
        assert b'Edit post: foo' in req.data

    def test_gallery(self):
        req = self.app.get('/gallery/')
        assert b'Gallery' in req.data

    def test_gallery_upload(self):
        req = self.app.get('/gallery/upload')
        assert b'Upload items' in req.data

    def test_calendar(self):
        req = self.app.get('/calendar/')
        assert b'Events' in req.data

    def test_calendar_new(self):
        req = self.app.get('/calendar/new')
        assert b'New event' in req.data

    def test_calendar_event(self):
        req = self.app.get('/calendar/foo')
        assert b'Edit event: foo' in req.data

if __name__ == '__main__':
    unittest.main()
