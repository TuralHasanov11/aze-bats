import os
from django.utils.translation import gettext as _, get_language, activate


def config_vars(request):
    return {
        "config_vars":{
            "phone": os.environ.get("PHONE", None),
            "email": os.environ.get("EMAIL", None),
        }
    }

def menu(request):
    lang = get_language()

    try:
        activate(language=lang)
        bats = _("bats")
    finally:
        activate(language=lang)
    return {
            "menu": {
                "bats": bats
            }
        }