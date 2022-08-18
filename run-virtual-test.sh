#!/bin/sh

cd "$(mktemp -d)"
python3 -m venv venv
source venv/bin/activate

rsync -vrtPh ~/nsh/oasa/* .
python3 ./setup.py build
python3 ./setup.py install
python3 -c 'import oasa'

python3 unittests.py
python3 test.py

deactivate
