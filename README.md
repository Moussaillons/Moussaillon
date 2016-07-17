# Moussaillon
A CMS for associations federations

## Installation
### Requirement
Python 3 and pip

### Environment

Note: since macos is crappy and everything, you need to adapt if you are using it

```
pip install virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
mkvirtualenv moussaillon
pip install -r requirements.txt
```

to be able to test subdomains, you need to modify the hosts file accordingly to your system and add:

```
127.0.0.1   federation.dev association.federation.dev
```

## Usage
### Launch local server
```
workon moussaillon
export FLASK_APP=moussaillon.py
export FLASK_DEBUG=1
cd moussaillon
flask run
```

### Test
Open [federation.dev](federation.dev) or [association.federation.dev](association.federation.dev) in your browser

### Leave environment
```
deactivate
```
