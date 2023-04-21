from django.http import Http404
from django.shortcuts import render, redirect
from .models import Snippet    
from MainApp.forms import SnippetForm
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

@login_required
def add_snippet_page(request):
    form = SnippetForm()

    if request.method == 'GET':

        context = {'pagename': 'Добавление нового сниппета',
                "form": form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                form.save()
            return redirect('snippets-list')
        return render(request, 'pages/add_snippet.html', {"form":form})


def snippets_page(request):

    snippets = Snippet.objects.filter(pablic=True)
    len_snippets = len(snippets)
    if request.user.is_authenticated:
        snippets = Snippet.objects.filter(user = request.user) | Snippet .objects.filter(pablic=True)
        
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets,
        "len_snippets": len_snippets
    }
    return render(request, 'pages/view_snippets.html', context)

@login_required
def my_snippets_page(request):
    snippets = Snippet.objects.filter(user = request.user) 

    return render(request, 'pages/view_snippets.html', {
        'pagename': 'Мои сниппеты',
        'snippets': snippets,
    })


def snippet_detail(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        return render(request, 'pages/snippet_detail.html', {
            'pagename': 'Просмотр сниппетов',
            'snippet': snippet,
            "type": "view",
        })
    except ObjectDoesNotExist:
        raise Http404

#def snippet_create(request):
#    if request.method == 'POST':
#        name = request.POST['name']
#        lang = request.POST['lang']
#        code = request.POST['code']
#        snippet = Snippet(name=name, lang=lang, code=code)
#        snippet.save()
#        return redirect('snippets-list')


def snippet_delete(request, id):
   Snippet.objects.get(id=id).delete()
   return redirect('snippets-list')

def login_page(request):
    if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       print("username =", username)
       print("password =", password)
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
           return render(request, "pages/index.html", {
               "errors": ["error login or pass"]
           })
           pass
    return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')


def snippet_edit(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        
    except ObjectDoesNotExist:
        raise Http404
    if request.method == 'GET':
        return render(request, 'pages/snippet_detail.html', {
            'pagename': 'Просмотр сниппетов',
            'snippet': snippet,
            "type": "edit"
        })
    if request.method == 'POST':
        form_data = request.POST
        snippet.name = form_data["name"]
        snippet.code = form_data["code"]
        snippet.creation_date = form_data["creation_date"]
        snippet.save()
        return redirect("snippets-list")