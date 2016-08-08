from flask import Flask
app = Flask(__name__)

app.config.from_pyfile('moussaillon_default_settings.cfg')
app.config.from_pyfile('server_config.cfg', silent=True)
