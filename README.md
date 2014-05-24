django-classification-banner
============================

A django app that adds classification banners to your site.

Installation
------------

The easiest way to install django-classification-banner is directly from PyPi using pip by running the command below:

```pip install django-classification-banner```

Otherwise you can download django-classification-banner and install it directly from source:

```python setup.py install```

Project Configuration
---------------------

Once installed you can configure your project to use the
django-classification-banner with the following steps.

Add ``django_classification_banner`` to ``INSTALLED_APPS`` in your project's
``settings`` module::

    INSTALLED_APPS = (
        # other apps
        'django_classification_banner',
    )

Add the classification banner context processor to the ```TEMPLATE_CONTEXT_PROCESSORS``` setting in your project's
``settings`` module::

    TEMPLATE_CONTEXT_PROCESSORS = (
        # other context processors
        "django_classification_banner.context_processors.classification",
    )

Customize your site's classification settings in the ``settings`` module:
	
	CLASSIFICATION_TEXT='Unclassified//FOUO'
	CLASSIFICATION_TEXT_COLOR='black'
	CLASSFICATION_BACKGROUND_COLOR='green'

Usage
-----

Once installed, you can easily add a classification banner to any template on your site.

First load the classification banner in your template:

	{% load classification_banner %}
	
Then add the banner to your page::

	{% classification_banner %}


A full example::

	{% load classification_banner %}
	<html>
		<head>
    		<title>FOO</title>
		</head>
		<body>
			{% classification_banner %}
		</body>
	</html>

You can also override your default settings from any template:

    {% load classification_banner %}
	<html>
		<head>
    		<title>FOO - Confidential</title>
		</head>
		<body>
			{% classification_banner classification_text='Confidential' classification_text_color='black' classification_background_color='red'%}
		</body>
	</html>
