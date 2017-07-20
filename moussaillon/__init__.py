from flask import Flask
app = Flask('moussaillon')

app.config.from_pyfile('moussaillon_default_settings.cfg')
app.config.from_pyfile('server_config.cfg', silent=True)

import moussaillon.routes
