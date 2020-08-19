# Django Templates
Django uses it's own templating engine similar to other popular python templating engine such as [Jinja2](https://palletsprojects.com/p/jinja/).

## Extends Templates
Header, Footer, navbar are similar in almost all the pages of our websites. So you can specify the repetating components in base templates and extends in other templates. For example: we are making our About us page and contact us page which has same headers and footer. So we define base template named ```app.html``` which includes header and footer and extends that ```app.html``` templates in about us and contact us page as.

```python
# File: templates/themes/app.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

# Prints the body section from child components as
{% block body %}{% endblock %}


<footer>
...
</footer>
</body>
</head>
``` 


Further, About us page can define in child template as:
```python
# File: templates/pages/about.html
{% extends "themes/app.html" %}

{% block body %}

# Write your about us specific body section
About use

{% endblock %}
```

In child template, we extend our template from base templates, and define body blocks, Which will yield in body section of base template. 

> Note: Here, in above examples, I have created base and child templates in themes and pages folder, which is optional. You can create templates in anywhere inside templates directory.


## Includes
Further, html component section can be written in separate files and later can include in our main templates. For example: header, navbar, footer such separate component can write in their own file and later include in main template as:
```python
# File: templates/themes/app.html
<!DOCTYPE html>
<html lang="en">

    # Including header section of layout
    {% include "themes/components/header.html" %}

    <title>Document</title>
<body>

# Including footer section of layout
{% include "themes/components/footer.html" %}

</body>
</head>
``` 
Now, Header, footer and similar othe separate components can define in separate files.
```python
# File: templates/themes/components/header.html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
```