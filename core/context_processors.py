import os
from django.utils.translation import gettext_lazy as _


def config_vars(request):
    return {
        "config_vars":{
            "phone": os.environ.get("OWNER_PHONE", None),
            "email": os.environ.get("OWNER_EMAIL", None),
        }
    }


def menu(request):
    return {
        "menu":{
            "home":{"route":"base:index", "text": _("Home")},
            "admin":[
                {"route":"administration:bat-list", "text": _("Bats")},
                {"route":"administration:project-list", "text": _("Projects")},
                {"route":"administration:visit-list", "text": _("Site visits")},
                {"route":"administration:article-list-create", "text": _("Articles")},
                {"route":"administration:author-list-create", "text": _("Our Researchers")}
            ],
            "activities":[
                {"route":"activities:projects", "text": _("Projects")},
                {"route":"activities:visits", "text": _("Site Visits")},
            ],
            "bats":{"route":"bats:index", "text": _("Bats")},
            "gallery":{"route":"bats:gallery", "text": _("Gallery")},
            "articles":{"route":"base:articles", "text": _("Articles")},
        }
    }