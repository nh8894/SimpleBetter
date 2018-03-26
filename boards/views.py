from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User

from .models import Board, Topic, Post
from .forms import NewTopicForm


class MyIndex(generic.TemplateView):
    template_name = 'boards/base.html'


class MyListView(generic.ListView):
    model = Board
    template_name = 'boards/list.html'
    context_object_name = 'boards'


class BoardDetail(generic.DetailView):
    model = Board
    template_name = 'boards/detail.html'
    context_object_name = 'board'


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board 
            topic.starter = user 
            topic.save()
            post = Post.objects.create(
                    message=form.cleaned_data.get('message'),
                    topic=topic,
                    created_by=user)
            return redirect('boards:board_detail', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})
#        subject = request.POST['subject']
#        message = request.POST['message']
#        user = User.objects.first() 
#        # TODO: get the currently logged in user
#
#        topic = Topic.objects.create(
#                subject=subject,
#                board=board,
#                starter=user
#        )
#
#        post = Post.objects.create(
#                message=message,
#                topic=topic,
#                created_by=user
#        )
#        return redirect('boards:board_detail', pk=board.pk)  # TODO: redirect to the created topic page
#    return render(request, 'boards/new_topic.html', {'board': board})
