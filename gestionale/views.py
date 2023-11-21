from django.http import HttpResponse
from gestionale.models import Esame, Paziente

def index(requets):
    p = Paziente()

    p.fiscalCode = 'BLDLRT02L23G914F'
    p.name = 'Alberto'
    p.surname = 'Baldin'
    p.save()

    e = Esame()

    e.valore = 10
    e.unita_misura = 'mg'
    e.paziente = p  
    e.save()

    return HttpResponse("Hello world! You are at the polls index.")