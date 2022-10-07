from django.utils.translation import gettext as _, get_language, activate

def nav(request):

    lang = get_language()

    try:
        activate(language=lang)
    finally:
        activate(language=lang)

    return {"admin_nav":[
        {"route":"administration:bat-list", "text": _("Bats")},
        {"route":"administration:project-list", "text": _("Projects")},
        {"route":"administration:visit-list", "text": _("Site visits")},
        {"route":"administration:article-list-create", "text": _("Articles")},
        {"route":"administration:author-list-create", "text": _("Our Researchers")}
    ]}

