django-classification-banner
============================

A django app that adds classification banners to your site.

Installation
============

* Add ```django_classification_banner``` to the INSTALLED_APPS tuple in your project.
* Make sure both template loaders and staticfiles finders includes app directories.
* Add ```CLASSIFICATION_TEXT```, ```CLASSIFICATION_TEXT_COLOR```,  and ```CLASSIFICATION_BACKGROUND_COLOR``` variables to your settings.py
    
    ```CLASSIFICATION_TEXT = 'UNCLASSIFIED'
    CLASSIFICATION_TEXT_COLOR = 'WHITE'
    CLASSIFICATION_BACKGROUND_COLOR = 'GREEN'```


* Add ```django_classification_banner.context_processors.classification``` to TEMPLATE_CONTEXT_PROCESSORS in settings.py
* Add ```{% load classification_banner %}``` to your template and then add the following template tag where you want the banner to show up ```{% classification_banner 'Unclassified' 'white' 'green'%}```.


