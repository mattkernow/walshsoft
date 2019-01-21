from django.template.loader import get_template
from django.http import HttpResponse


def cv(request):
    t = get_template('cv.html')
    html = t.render()
    return HttpResponse(html)
