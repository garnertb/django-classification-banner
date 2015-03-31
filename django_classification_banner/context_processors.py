from django.conf import settings


def classification(request):
    """
    Adds classification context to views.
    """

    ctx = {
        'classification_text': getattr(settings, 'CLASSIFICATION_TEXT', 'UNCLASSIFIED'),
        'classification_text_color': getattr(settings, 'CLASSIFICATION_TEXT_COLOR', 'white'),
        'classification_background_color': getattr(settings, 'CLASSIFICATION_BACKGROUND_COLOR', 'green'),
        'classification_banner_enabled': getattr(settings, 'CLASSIFICATION_BANNER_ENABLED', True),
        'classification_link': getattr(settings, 'CLASSIFICATION_LINK', None)
    }

    return ctx
