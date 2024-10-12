# app/main/views.py

# Django modules
from django.http import HttpResponse
import datetime


def halodunia(request):
    now = datetime.datetime.now()
    html = "<html><body>Halo Dunia!<br> Waktu Jakarta sekarang adalah %s.</body></html>" % now
    return HttpResponse(html)