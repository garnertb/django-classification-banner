from django import template
from django.core.urlresolvers import reverse, reverse_lazy

register = template.Library()

@register.inclusion_tag('django_classification_banner/classification.html', takes_context=True)
def classification_banner(context, **kwargs):
    response = dict()

    for var in ['classification_text', 'classification_text_color', 'classification_background_color']:
        response[var] = kwargs.get(var, context.get(var))

    return response



