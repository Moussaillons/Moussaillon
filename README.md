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

## Usage
### Launch local server
```
workon moussaillon
cd moussaillon
flask run
```

### Leave environment
```
desactivate
```
