from django.http import HttpResponse


def index(request):
    txt="<b>I am at Project Level index.... !!!</b>"
    return HttpResponse(txt)