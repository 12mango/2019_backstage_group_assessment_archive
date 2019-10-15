from django.shortcuts import render
from django.http import HttpResponse
from newsApp.models import news

def table(request):
    title = request.GET['title']
    sdate = request.GET['sdate']
    tdate = request.GET['tdate']
    preType = request.GET.getlist('type')
    order = int(request.GET['order'])
    type = [int(x) for x in preType]
    info = news.objects.filter(title__icontains=title, type__in=type, date__gte=sdate, date__lte=tdate)

    if order == 0:
        info = info.order_by('-date')
    else:
        info = info.order_by('date')

    return render(request, 'table.html', {'data': info})

def tableAll(request):
    info=news.objects.all()
    return render(request,'table.html',{'data':info})

def index(request):
    return render(request, 'index.html')