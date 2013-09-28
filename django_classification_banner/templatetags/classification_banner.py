from django import template
from django.core.urlresolvers import reverse, reverse_lazy

register = template.Library()

@register.inclusion_tag('django_classification_banner/classification.html', takes_context=True)
def classification_banner(context, **kwargs):

    params = context.update(kwargs)

    return dict(classification_text=params.get('classification_text'),
                classification_text_color=params.get('classification_text_color'),
                classification_background_color=params.get('classification_background_color'),
                )



