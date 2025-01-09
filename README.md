# OneLastMerch

School project. Website/shop containing various merch from *OneLast*

## IMPORTANT NOTES

OneLastMerch -> project that has shop-like features, featuring *OneLast*. OneLast was a SCI++ (school) project.
This project uses 100% Django. Also uses .env which makes it quite hard to copy, and debug without deployment with which i have a lot of issues.|
On Vercel and locally in Debug = False (the production mode) the static files were not loading correctly.
Now it fails on Render, because it doessn't see module "OneLastMerch/OneLastMerch.asgi:application"

### Commits

Some commits are only readable with this explanation:
The commits about Vercel/Json were all made to just refresh the Vercel and push some very little changes, that I thought were causing so many issues.
These commits don't have any real value in the project aside making my mind go crazy at times.

### Creator

Jakub Kulik
3C

### Some code explanation

The project as said before uses 100% [Django](https://docs.djangoproject.com/en/5.1/). I used the Django templates and normal CSS (no JS frameworks nor any Tailwind)
Tried to make the page intuitive, by using well-known designs.
The project contains of 4 apps:

- OneLastMerch (main app), that shows the view
- utils (side app), only there for |add_class filter for Django templates, it is in "templatetags" directory at custom_filters.py. It has comments on what it does.
- auth (authorization app), has the entire login, registration and logic + UX/UI
- ui (app for shop and account), used mainly to display the user-visible stuff
