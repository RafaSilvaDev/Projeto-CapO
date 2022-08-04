from ssl import OP_NO_RENEGOTIATION
from django.shortcuts import render, redirect
from home.models import Parametros
from django.core.mail import send_mail



# Create your views here.
def index(request):
  return render(request, 'home/index.html')

def sent(request):
  return render(request, 'home/sent.html')

def saveParametros(request):
  if str(request.method) == "POST":
    gbGrp = request.POST.get("gbgroup")
    mailTo = request.POST.get("mailto")
    Parametros.objects.create(gb=gbGrp, mailTo=mailTo)

    send_mail(
      'Assunto', #assunto
      'Mensagem', #mensagem
      'rafabdasilva12@gmail.com', #de
      ['rafabdasilva12@gmail.com'], #para
      fail_silently=False,
    )
    # redirect para evitar uma nova inserção no banco ao atuazar a página
    return redirect('sent')
  
  return render(request, 'home/sent.html')
  
def getData(request):
  dados = Parametros.objects.latest('id')
  gb = str(dados).split('|')[0]
  mail = str(dados).split('|')[1]
  print(f'Grupo: {gb} | email: {mail}')
  return render(request, 'home/getData.html', {'gb':gb, 'mail':mail})