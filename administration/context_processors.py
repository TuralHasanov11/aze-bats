def nav(request):
    return {"admin_nav":[
        {"route":"administration:bat-list", "text":"Bats"},
        {"route":"administration:project-list", "text":"Projects"},
        {"route":"administration:visit-list", "text":"Site visits"},
        {"route":"administration:article-list-create", "text":"Articles"},
        {"route":"administration:author-list-create", "text":"Our Researchers"}
    ]}