# Exit on error
set -o errexit

cd OneLastMerch/

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

chmod -R 755 ./OneLastMerch/OneLastMerch/staticfiles
