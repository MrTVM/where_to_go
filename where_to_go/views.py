# base lib

# custom lib
from django.http import HttpResponse
from django.template import loader

# local lib


def show_index(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
