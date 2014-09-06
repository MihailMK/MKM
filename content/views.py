from django.shortcuts import render_to_response
from content.models import Content


def index (request, content_id = 1):
    return render_to_response ( 'content.html', { 'content' : Content.objects.get ( id = content_id ) } )