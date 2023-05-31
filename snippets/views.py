from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet
from .forms import SnippetForm


def snippet_list(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippet_list.html', {'snippets': snippets})
