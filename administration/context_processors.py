from django.utils.translation import gettext as _, get_language, activate

def nav(request):
    lang = get_language()
    try:
        activate(language=lang)
    finally:
        activate(language=lang)

    return {}

