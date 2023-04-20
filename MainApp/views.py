from django.http import Http404
from django.shortcuts import render, redirect
from .models import Snippet    
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    form = SnippetForm()

    if request.method == 'GET':

        context = {'pagename': 'Добавление нового сниппета',
                "form": form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets-list')
        return render(request, 'pages/add_snippet.html', {"form":form})

def snippets_page(request):
    snippets = Snippet.objects.all()
    len_snippets = len(snippets)
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets,
        "len_snippets": len_snippets
    }
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, id):
    snippet = Snippet.objects.get(id=id)
    return render(request, 'pages/snippet_detail.html', {
        'pagename': 'Просмотр сниппетов',
        'snippet': snippet,
    })

#def snippet_create(request):
#    if request.method == 'POST':
#        name = request.POST['name']
#        lang = request.POST['lang']
#        code = request.POST['code']
#        snippet = Snippet(name=name, lang=lang, code=code)
#        snippet.save()
#        return redirect('snippets-list')


def create_snippet(request):
   form = SnippetForm()
   return render(request, 'add_snippet.html', {'form': form})
