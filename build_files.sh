#!/bin/bash

# Install Python dependencies
python -m pip install -r OneLastMerch/requirements.txt
python OneLastMerch/manage.py collectstatic --noinput
