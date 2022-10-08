import os

def config_vars(request):
    return {
        "config_vars":{
            "phone": os.environ.get("PHONE", None),
            "email": os.environ.get("EMAIL", None),
        }
    }