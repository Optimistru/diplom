from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic

class task_list(generic.ListView):
    template_name = 'tasks/list.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Return all tasks sort by name"""
        return Problem.objects.order_by('name')


class task_details(generic.DetailView):
    model = Problem
    template_name = 'tasks/detail.html'


class task_edit(generic.DetailView):
    model = Problem
    template_name = 'tasks/edit.html'


def task_delete(request, task_id):
    task = get_object_or_404(Problem, pk=task_id)
    try:
        Problem.objects.filter(id=task_id).delete()
    except ():
        return render(request, 'tasks/detail.html', {
            'question': task,
            'message': "Error occured",
        })
    else:
        return render(request, 'tasks/detail.html', {
            'question': task,
            'message': "Deleted",
        })