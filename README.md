# Moussaillon [![Build Status](https://travis-ci.org/Moussaillons/Moussaillon.svg?branch=master)](https://travis-ci.org/Moussaillons/Moussaillon)
A CMS for associations federations

## Installation
### Requirement
Python 3 and pip

### Environment

_Note: since macos is crappy and everything, you need to adapt if you are using it._

```
pip install virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
mkvirtualenv moussaillon
pip install -r requirements.txt
```
You may have to change the `SERVER_NAME` variable in the `moussaillon.py` file in order to navigate on the website correctly.

To be able to test subdomains, you need to modify the hosts file accordingly to your system and add:

```
127.0.0.1   federation.dev association.federation.dev
```

## Usage
### Launch local server automatically
```
./launch_server.sh
```

### Launch local server manually
```
workon moussaillon
export FLASK_APP=moussaillon.py
export FLASK_DEBUG=1
cd moussaillon
flask run
```

### Test
Open [federation.dev](http://federation.dev:5000) or [association.federation.dev](http://association.federation.dev:5000) in your browser

### Leave environment
```
deactivate
```
