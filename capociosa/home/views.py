from django.shortcuts import render
from home.models import Parametros

# Create your views here.
def index(request):
  return render(request, 'home/index.html')

def saveParametros(request):
  gbGrp = request.POST.get("gbgroup")
  mailTo = request.POST.get("mailto")

  Parametros.objects.create(gb=gbGrp, mailTo=mailTo)

  dados = Parametros.objects.latest('id')
  gb = str(dados).split('|')[0]
  mail = str(dados).split('|')[1]
  
  return render(request, 'home/sent.html')
  
