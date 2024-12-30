#!/bin/bash

# Install Python dependencies
python3 -m pip install -r OneLastMerch/requirements.txt

# Collect static files into the 'OneLastMerch/staticfiles' directory
python3 OneLastMerch/manage.py collectstatic --noinput
