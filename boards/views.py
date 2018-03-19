from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Board, Topic
from .form import NewTopicForm 

class MyIndex(generic.TemplateView):
    template_name = 'boards/index.html'


class MyListView(generic.ListView):
    model = Board
    template_name = 'boards/list.html'
    context_object_name = 'boards'


class BoardDetail(generic.DetailView):
    model = Board
    template_name = 'boards/detail.html'
    context_object_name = 'board'


class BoardNew(generic.CreateView):
    model = Board 
    template_name = 'boards/new.html'
    context_object_name = 'board'
    form = NewTopicForm

