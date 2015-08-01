from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect,HttpResponse
from funcionario.models import Funcionario
from questionario.models import Questionario, Questionario_Questao,Questao, Resposta
from planejamento.models import Planejamento
from django.views.generic import TemplateView
from reportlab.pdfgen import canvas
#from report import write_to_pdf
from django.contrib.auth.decorators import login_required


def appweb_home(request):
	return render(request,'login.html')


def home(request):
    data = {}
    if 'username' in request.POST :
        if request.POST['username'] != '':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
                 
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.user.is_superuser:
                        return render(request,'home.html',data)  
                    else:
                        func = Funcionario.objects.get(usuario_id=request.user) 
                        data['nome_func'] = func.nome
                        Planej  = Planejamento.objects.filter(avaliador_id=func.id,status= False)
                        data['plan'] = Planej
                        #quest   = Questionario.objects.filter(id__in=[list(Planej)])
                        #for plan in Planej:
                        #    quest = Questionario.objects.filter(id=plan.questionario_id)
                        #    lista.append(quest)
                        
                        return render(request,'home.html',data)
             
                else:
                    return render(request,'login.html')
            else:
                return render(request,'login.html')
    else:
        func = Funcionario.objects.get(usuario_id=request.user) 
        data['nome_func'] = func.nome
        Planej  = Planejamento.objects.filter(avaliador_id=func.id,status= False)
        data['plan'] = Planej
        return render(request,'home.html',data)

    

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
    #return render(request,'login.html',data)
   
def questionario(request,id):
    data = {}
    plan  = Planejamento.objects.get(id=id)
    quest = Questionario.objects.get(id=plan.questionario_id)
    #qquestionario = Questionario_Questao.objects.filter(idquestionario=quest.id)
    qquestionario = Questionario_Questao.objects.filter(idquestionario_id=quest.id)
    questoes = Questao.objects.all()
    data['quest'] = quest
    data['qquest'] = qquestionario
    data['questoes'] = questoes
    data['plan']    = plan 
    return render(request,'questionario.html',data)

def salvarQuestionario(request):
    data={}
    questionario = request.POST['pkquestionario']
    questao      = Questao.objects.all()
    func         = request.POST['pkfuncionario']
    avaliador    = request.POST['pkavaliador']
    planeid     = request.POST['pkplan']
    values = request.POST.getlist('pkquestao')

    for questao in values :    
        Resp = Resposta(questionario_id = questionario,
                        questao_id      = questao,
                        resposta        = request.POST[questao],
                        funcionario_id  = func,
                        avaliador_id    = avaliador )
       
        Resp.save()
    
    planej = Planejamento.objects.get(id =planeid) 
    planej.status = True
    planej.save()

    return render(request,'home.html')


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    Quest = Questao.objects.all();
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    usuario = request.user
    p.drawString(100, 100, "usuario")
    p.drawString(10,20, Quest)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

# aqui ira chamar  template com a lista em html
def lista_resposta(request):
    data = {}
    func       = Funcionario.objects.get(usuario_id = request.user.pk)
    planejs    = Planejamento.objects.filter(funcionario_id = func) 
    questionas = Questionario.objects.filter(id__in= planejs)
    resp = Resposta.objects.filter(funcionario_id = func)
    data['questionas'] = questionas
    data['planejs'] = planejs
    data['respostas'] = resp.count
    data['nome_func'] = func.nome
    return render(request,'relatorio.html',data) 

#aqui ira gerar o pdf a partir do template 
def listar_respostas(request):
    resp = Resposta.objects.all()
    return write_to_pdf('relatorio.html', {'clientes': clientes}, 'nome_do_arquivo_pdf')

    