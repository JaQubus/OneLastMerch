# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r OneLastMerch/requirements.txt

# Convert static asset files
python OneLastMerch/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python OneLastMerch/manage.py migrate