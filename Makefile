ENVDIR = env
VIRTUALENV = virtualenv
PIP = $(ENVDIR)/bin/pip
TOX = $(ENVDIR)/bin/tox
NOSE = $(ENVDIR)/bin/nosetests
PANDOC = $(ENVDIR)/bin/pandoc
PYTHON = $(ENVDIR)/bin/python

COV_OPTS = --with-coverage --cover-package=maxcdn,tests --cover-tests

init: clean test

virtualenv:
	$(VIRTUALENV) $(ENVDIR)

requirements: virtualenv
	$(PIP) install -r requirements.txt

test: requirements
	$(TOX) -- tests/

integration-test: requirements
	$(NOSE) tests/int.py

coverage: requirements
	$(NOSE) $(COV_OPTS) tests/

clean:
	rm -rf .ropeproject .coverage junit-report.xml .tox $(ENVDIR)
	find . -type f -name "*.pyc" -delete

travis: test

readme:
	$(PANDOC) -s -t rst --toc README.md  |grep -v "Build\|Status" > README.text

upload: readme
	$(PYTHON) setup.py sdist register upload

.PHONY: clean virtualenv test coverage requirements travis readme upload init
