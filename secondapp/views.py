from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

# Create your views here.

def main(request):
    return HttpResponse('main!')

def index1(request):
    return HttpResponse('index1')

def show(request):
    hospital = Hospital.objects.all()
    return render(request, 'show.html', {'list':hospital})
    # html = ''
    # for c in curriculum:
    #     html += '%s번 %s<br>' % (c.id, c.name)
    # return HttpResponse(html)