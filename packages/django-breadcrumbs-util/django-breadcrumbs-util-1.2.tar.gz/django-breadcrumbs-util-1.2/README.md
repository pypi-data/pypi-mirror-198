
# Django Breadcrumbs Utils


Django Breadcrumbs Utils is a package that provides a simple way to add breadcrumbs to your Django views.

Installation
You can install the package via pip:
## Deployment

To deploy this project run

```python
  pip install django-breadcrumbs-utils

```

## Usage
To use the custom_path function from the package, import it into your urls.py file and use it to define your URL patterns:


```python
from breadcrumbs import custom_path

urlpatterns = [
    custom_path('my-route/', my_view, name='my-view', breadcrumb='My View'),
    # ...
]

```

The custom_path function takes a route argument, a view function, a name argument (optional), and a breadcrumb argument (optional).

The breadcrumb argument should be a string that represents the label of the breadcrumb for the current page.

The custom_path function wraps your view function with a decorator that adds a breadcrumb variable to the context of the view function. The variable contains the breadcrumb label specified in the breadcrumb argument.

## In your template
you can access the breadcrumb variable to display the breadcrumb:


```html
{% block breadcrumbs %}
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="/">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ breadcrumb }}</li>
  </ol>
</nav>
{% endblock %}

```

This will display a breadcrumb trail that starts with a link to the home page and ends with an active breadcrumb label for the current page.
