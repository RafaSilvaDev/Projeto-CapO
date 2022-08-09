import os
from urllib import response
from django.shortcuts import render, redirect
from home.models import Parametros
import pythoncom
import win32com.client as win32
from django.http import HttpResponse

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

    # primeiro email informando que entra na fila

    pythoncom.CoInitialize()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = f'{mailTo}'
    mail.Subject = 'Automação iniciada'
    mail.Body = 'A automação foi engatilhada para a fila de execução na Fastlane (ambiente de execução de automações em nuvem). Aguarde por mais informações a respeito da execução do processo.'

    mail.Send()

    # segundo email para gatilho da automação
    pythoncom.CoInitialize()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'GS.FastlaneEmailTrigger@de.bosch.com'
    mail.Subject = 'PS\ETS_PS_LA_Automated confirmation of Otiose Capacity debits in SAP_f2dab395-d383-4826-8cb2-e8382a1c071c\Teste_BOT|10'
    # mail.Subject = 'PS\ETS_PS_LA_Automated confirmation of Otiose Capacity debits in SAP_f2dab395-d383-4826-8cb2-e8382a1c071c\BOT_Capacidade-Ociosa|50'
    # mail.Body = 'Message body'
    # mail.HTMLBody = '<h2>HTML Message body</h2>'

    mail.Send()
    # redirect para evitar uma nova inserção no banco ao atuazar a página
    return redirect('sent')
  
  return render(request, 'home/sent.html')
  
def getPage(request):
  return render(request, 'home/getPage.html')


def getData(request):
  dados = Parametros.objects.latest('id')
  gb = str(dados).split('|')[0]
  mail = str(dados).split('|')[1]
  # print(f'Grupo: {gb} | email: {mail}')

  xresponse = HttpResponse(content_type='text/plain') 
  xresponse['Content-Disposition'] = 'attachment; filename=parameters.txt'
  
  lines = [
    f'{gb}\n',
    f'{mail}',
  ]

  xresponse.writelines(lines)

  return xresponse