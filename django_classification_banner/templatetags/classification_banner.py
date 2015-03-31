from django import template

register = template.Library()


@register.inclusion_tag('django_classification_banner/classification.html', takes_context=True)
def classification_banner(context, **kwargs):
    response = dict()

    for var in ['classification_text', 'classification_text_color', 'classification_background_color',
                'classification_banner_enabled', 'classification_link']:
        response[var] = kwargs.get(var, context.get(var))

    return response
