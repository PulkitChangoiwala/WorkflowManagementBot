
from django.http import HttpResponse


def g_sheet_importer(request):
    print("I will import from google sheets")
    return HttpResponse('Hello World')

