from django.shortcuts import redirect, render 
from players.forms import JogadoresForm
from players.models import jogadores 


def home(request):
    data = {}
    data['db'] = jogadores.objects.all()
    return render(request, 'index.html', data )


def form(request):
    data = {}
    data['form'] = JogadoresForm()
    return render(request, 'form.html', data )


def create(request):
    form = JogadoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data ['db'] = jogadores.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data ['db'] = jogadores.objects.get(pk=pk)
    data['form'] = JogadoresForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = jogadores.objects.get(pk=pk)
    form = JogadoresForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db =  jogadores.objects.get(pk=pk)
    db.delete ()
    return redirect('home')
