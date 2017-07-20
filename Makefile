APP_NAME=moussaillon
.PHONY: clean

all: setup debug.sh

setup.sh:
	echo "#!/bin/sh" > $@
	echo "virtualenv-3 .venv" >> $@
	echo ". .venv/bin/activate" >> $@
	echo "pip install --editable ." >> $@
	echo "sqlite3 moussaillon.db < schema.sql" >> $@
	echo "deactivate" >> $@
	chmod a+x $@

debug.sh:
	echo "#!/bin/sh" > $@
	echo ". .venv/bin/activate" >> $@
	echo "export FLASK_APP=$(APP_NAME)" >> $@
	echo "export FLASK_DEBUG=true" >> $@
	echo "flask run" >> $@
	echo "deactivate" >> $@
	chmod a+x $@

setup $(APP_NAME).egg-info .venv: setup.sh
	# we need an environement change
	# Therefor everything should be donne at the same level
	# Because a child can't modify its parent env
	# we need to do everything at the same level
	./setup.sh
	echo "please add the two following lines to /etc/hosts"
	echo "127.0.0.1 federation.dev echo.federation.dev hazybot.federation.dev"
	echo "::1 federation.dev echo.federation.dev hazybot.federation.dev"
	echo "if you have a better solution than this, please tell"

run: debug.sh $(APP_NAME).egg-info
	# same rationale as the setup scenario
	./debug.sh

clean:
	@-rm -R setup.sh debug.sh .venv $(APP_NAME).egg-info moussaillon.db ||:
