from django.shortcuts import render
from .models import *

def index(request):
    intro = Intro.objects.get(pk=1)
    we = We.objects.get(pk=1)
    service = Service.objects.all()
    problems = Problems.objects.get(pk=1)
    needs =Needs.objects.get(pk=1)
    person = Person.objects.all()
    spec = Specializations.objects.all()
    talks = Talks.objects.all()
    return render(request, 'biipeco/index.html', {'intro': intro, 'we': we, 'service': service, 'problems': problems, 'needs': needs, 'person': person, 'spec': spec,
                                                  'talks': talks})

def contacts(request):
    maps = Maps.objects.all()
    licenses = Licenses.objects.all()
    return render(request, 'biipeco/contacts.html', {'maps': maps, 'licenses': licenses})

def air(request):
    return render(request, 'biipeco/air.html')

def eco_report(request):
    return render(request, 'biipeco/eco_report.html')

def  ecology(request):
    return render(request, 'biipeco/ecology.html')

def refuse(request):
    return render(request, 'biipeco/refuse.html')

def water(request):
    return render(request, 'biipeco/water.html')
