#!/bin/sh

workon moussaillon
export FLASK_APP=moussaillon.py
export FLASK_DEBUG=1
cd moussaillon
flask run
cd ..
