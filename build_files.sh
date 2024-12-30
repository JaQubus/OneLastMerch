#!/bin/bash

# Install Python dependencies
python3 -m pip install -r OneLastMerch/requirements.txt
python3 OneLastMerch/manage.py collectstatic --noinput
