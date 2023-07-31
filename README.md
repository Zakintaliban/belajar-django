`__init__.py` is empty, but it is required to make Python treat the directories as containing packages.
`asgi.py` and `wsgi.py` are entry points for WSGI-compatible web servers to serve the project.
`settings.py` contains the configuration of the project.
`urls.py` contains the URL declarations for the project.
`manage.py` is a command-line utility that lets you interact with this Django project in various ways.
`admin.py` is a configuration file for the built-in Django Admin app.
`apps.py` is a configuration file for the app itself.
`models.py` is a configuration file for the database.
`tests.py` is a configuration file for the tests.
`views.py` is a configuration file for the views.

## html template

put it in `templates` folder
`base.html` is the base template for all other templates.
block is used to override the content in base.html
example

`base.html`

```html
...
    <title>{% block title %}Document{% endblock %}</title>
    </head>
    <body>
        <div class="container">{% block content %} {% endblock %}</div>
    </body>
```

`home.html`

```html
{% extends "base.html" %} {% block title %} HomePage {% endblock %} {% block content %}
<h1>Welcome to my blog</h1>
<p>This is my first blog post</p>
{% endblock %}
```
