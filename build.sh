#!/usr/bin/env bash

if [ ! -d venv ]; then
    python -m venv venv
    python -m pip install --upgrade pip
    pip install -r requirements-dev.txt
fi

. venv/bin/activate
python setup.py sdist bdist_wheel
