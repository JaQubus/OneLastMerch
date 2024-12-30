#!/bin/bash

# Install Python dependencies
python3 -m pip install -r OneLastMerch/requirements.txt

# Collect static files into the root-level 'staticfiles' directory
python3 OneLastMerch/manage.py collectstatic --noinput --settings=OneLastMerch.settings
