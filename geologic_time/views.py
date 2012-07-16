from django.shortcuts import render_to_response
from django.template import RequestContext as RC

def home( request ):
    return render_to_response(
        'index.html',
        {},
        context_instance = RC( request, {} ),
    )

def help(request):
    return render_to_response(
        'help.html',
        {},
        context_instance = RC(request,{}),
    )

def config(request):
    return render_to_response(
        'config.html',
        {},
        context_instance = RC(request,{}),
    )

def alerts(request):
    return render_to_response(
        'alerts.html',
        {},
        context_instance = RC(request, {}),
    )
