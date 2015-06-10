from django.shortcuts import render
from .models import Temp

from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    #index = Temp.objects.filter(time_measured__isnull=False).order_by('time_measured')
    latest_temps_list = Temp.objects.order_by('-time_measured')[:5]
    #template = loader.get_template('djangoblaz/index.html')
    context = RequestContext(request, {'latest_temps_list': latest_temps_list,})
    device_name = 'ESP8266'
    #return HttpResponse (template.render(context))
    return render(request, 'blaziot/temp_list_index.html', {'temps':latest_temps_list, 'device':device_name})
    #return HttpResponse("Hi Blaz! Here are your latest measurements.")

def temp_list(request):
    temps = Temp.objects.filter(time_measured__isnull=False).order_by('time_measured')
    return render(request, 'blaziot/temp_list.html', {'temps':temps})
    
    
#def post_list(request):
#    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})
