from django.shortcuts import render,get_object_or_404
from .models import Person
from .forms import  PersonForm
from .gsheetImport import g_sheet_importer
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.


def persons_list(request):

    persons = Person.objects.all()
    return render(request, 'persons/persons_list.html', {'persons': persons})


def searchResult(request):
    if request.method == "POST":
        name = request.POST['search_name']
        company =  request.POST['search_company']
        designation =  request.POST['search_designation']

        if name and company and designation:
          persons = Person.objects.filter(name__icontains=name).filter(company__icontains=company).filter(designation__icontains=designation)
        elif name and company and not designation:
            persons = Person.objects.filter(name__icontains=name).filter(company__icontains=company)
        elif name and not company and designation:
            persons = Person.objects.filter(name__icontains=name).filter(designation__icontains=designation)
        elif not name and company and designation:
            persons = Person.objects.filter(company__icontains=company).filter(designation__icontains=designation)
        elif name:
            persons = Person.objects.filter(name__icontains=name)
        elif company:
            persons = Person.objects.filter(company__icontains=company)
        elif designation:
            persons = Person.objects.filter(designation__icontains=designation)
        else:
            persons = Person.objects.all()




    else:
        name= " "
        persons = []
    return render(request, 'persons/persons_searchList.html', {'persons': persons})


def fillDetailForm(request):
    form = PersonForm(request.POST)
    if(form.is_valid()):
        form.save()
    return render(request, 'persons/form.html', {'form': form})


def g_sheet_import(request):
    return g_sheet_importer(request)