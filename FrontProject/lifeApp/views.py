from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Topic,WebPage,AccessRecord

def index(request):
    txt='I am at the App level Index '
    return HttpResponse(txt)
    
def renindex(request):
    my_dict={'my_text':'Hello...Loading Static FIles'}
    return render(request,'lifeAPP/index.html',context=my_dict)

def topics(request):
    top=AccessRecord.objects.order_by('date')
    topic_urls={'all_records': top}
    return render(request,'lifeAPP/home.html',context=topic_urls)

    
        
        
