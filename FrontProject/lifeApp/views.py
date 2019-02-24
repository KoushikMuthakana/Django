from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    txt='I am at the App level Index '
    return HttpResponse(txt)
    
def renindex(request):
    my_dict={'my_text':'Hello...Loading Static FIles'}
    return render(request,'lifeAPP/index.html',context=my_dict)