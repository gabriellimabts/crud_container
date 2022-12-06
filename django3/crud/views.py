from django.shortcuts import render
from .models import Pessoa
from django.views.decorators.csrf import csrf_protect

def listagem(request):
	titulo = 'Listagem de Contêiners'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def selecao(request, id):
	titulo = 'Listagem de Contêiners'
	pessoa = Pessoa.objects.get(id=id)
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': [pessoa]})

@csrf_protect
def consulta(request):
	consulta = request.POST.get('consulta')
	campo = request.POST.get('campo')

	if campo   == 'cliente':
		pessoas = Pessoa.objects.filter(cliente__contains=consulta)
	elif campo == 'numero_conteiner':
		pessoas = Pessoa.objects.filter(numero_conteiner__contains=consulta)
	elif campo == 'tipo':
		pessoas = Pessoa.objects.filter(tipo__contains=consulta)
	elif campo == 'status':
		pessoas = Pessoa.objects.filter(status__contains=consulta)
	elif campo == 'categoria':
		pessoas = Pessoa.objects.filter(categoria__contains=consulta)
	elif campo == 'movimentacao':
		pessoas = Pessoa.objects.filter(movimentacao__contains=consulta)
	elif campo == 'data_inicial':
		pessoas = Pessoa.objects.filter(data_inicial__contains=consulta)
	elif campo == 'data_final':
		pessoas = Pessoa.objects.filter(data_final__contains=consulta)

	titulo = 'Listagem de Contêiners'
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

_campo = ''
def ordenacao(request, campo):
	titulo = 'Listagem de Contêiners'
	global _campo
	if campo == _campo:
		pessoas = Pessoa.objects.all().order_by(campo).reverse()
		_campo = ''
	else:
		pessoas = Pessoa.objects.all().order_by(campo)
		_campo = campo
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def insercao(request):
	titulo = 'Inserção de Contêiner'
	return render(request, 'insercao.html', {'titulo': titulo})

@csrf_protect
def salvar_insercao(request):
	cliente = request.POST.get('cliente')
	numero_conteiner = request.POST.get('numero_conteiner')
	tipo = request.POST.get('tipo')
	status = request.POST.get('status')
	categoria = request.POST.get('categoria')
	movimentacao = request.POST.get('movimentacao')
	data_inicial = request.POST.get('data_inicial')
	data_final = request.POST.get('data_final')
	
	

	objeto = Pessoa(
		cliente=cliente,
		numero_conteiner=numero_conteiner,
		tipo=tipo,
		status=status,
		categoria=categoria,
		movimentacao=movimentacao,
		data_inicial=data_inicial,
		data_final=data_final,
		
		
	)
	objeto.save()

	titulo = 'Listagem de Contêiners'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def edicao(request, id):
	titulo = 'Edição de Contêiner'
	pessoa = Pessoa.objects.get(id=id)
	return render(request, 'edicao.html', {'titulo': titulo, 'pessoa': pessoa})

@csrf_protect
def salvar_edicao(request):
	id = request.POST.get('id')
	cliente = request.POST.get('cliente')
	numero_conteiner = request.POST.get('numero_conteiner')
	tipo = request.POST.get('tipo')
	status = request.POST.get('status')
	categoria = request.POST.get('categoria')
	movimentacao = request.POST.get('movimentacao')
	data_inicial = request.POST.get('data_inicial')
	data_final = request.POST.get('data_final')
	
	

	Pessoa.objects.filter(id=id).update(
		cliente=cliente,
		numero_conteiner=numero_conteiner,
		tipo=tipo,
		status=status,
		categoria=categoria,
		movimentacao=movimentacao,
		data_inicial=data_inicial,
		data_final=data_final,
		)

	titulo = 'Listagem de Contêiners'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def delecao(request, id):
	titulo = 'Deleção de Contêiner'
	pessoa = Pessoa.objects.get(id=id)
	return render(request, 'delecao.html', {'titulo': titulo, 'pessoa': pessoa})

@csrf_protect
def salvar_delecao(request):
	id = request.POST.get('id')

	Pessoa.objects.filter(id=id).delete()

	titulo = 'Listagem de Contêiners'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

