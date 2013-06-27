from django.conf import settings


def classification(request):
    """
    Adds classification context to views.
    """

    ctx = {
        "CLASSIFICATION_TEXT": getattr(settings, "CLASSIFICATION_TEXT"),
        "CLASSIFICATION_TEXT_COLOR": getattr(settings,"CLASSIFICATION_TEXT_COLOR"),
        "CLASSIFICATION_BACKGROUND_COLOR": getattr(settings,"CLASSIFICATION_BACKGROUND_COLOR")
    }

    return ctx