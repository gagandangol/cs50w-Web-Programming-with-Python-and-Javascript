import random

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from markdown2 import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def pages(request, title):

    entry = util.get_entry(title)
    
    if entry is None:
        return HttpResponse("Page Not Found.")
    
    context = markdown(entry)
    return render(request, "encyclopedia/pages.html", {
        "context": context,
        "title": title
    })

def random_page(request):

    title = random.choice(util.list_entries())
    entry = util.get_entry(title)
    context = markdown(entry)
    return render(request, "encyclopedia/pages.html", {
        "context": context,
        "title": title
    })


def create_page(request):

    if request.method == 'GET':
        return render(request, "encyclopedia/add.html")

    if request.method == 'POST':
        data = request.POST.get('data', '')
        title = request.POST.get('title').strip()
    
        util.save_entry(title, data)
        
        return redirect('wiki/' + str(title))

def search(request):

    query = request.Get.get('q')
    wiki_entries = util.list_entries()

    for wiki_entry in wiki_entries:
        if wiki_entry.lower() == query.lower():
            return redirect('wiki/' + str(query))
    else:
        pass

