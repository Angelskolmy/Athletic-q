from django.shortcuts import render

def index_compilate(request): 

    return render (request, "templates_core_session/index.html")
