from django import template
from django.core.urlresolvers import reverse, reverse_lazy

register = template.Library()

@register.simple_tag
def classification_banner(classification_text, classification_text_color, classification_background_color, **kwargs):

    resp = kwargs
    resp['CLASSIFICATION_TEXT'] = classification_text
    resp['CLASSIFICATION_TEXT_COLOR'] = classification_text_color
    resp['CLASSIFICATION_BACKGROUND_COLOR'] = classification_background_color

    return resp

register.inclusion_tag('django_classification_banner/classification.html')(classification_banner)
