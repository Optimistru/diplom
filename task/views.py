from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *
from django.views import generic

# class ProblemModificationForm(forms.ModelForm):
#     class Meta:
#         model = ProblemModification
#         fields = '__all__'

class task_list(generic.ListView):
    template_name = 'task/list.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Return all tasks sort by name"""
        return Problem.objects.order_by('name')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(task_list, self).get_context_data(**kwargs)
        context['fields'] = Problem._meta.get_fields()
        return context


class task_details(generic.DetailView):
    model = Problem
    template_name = 'task/detail.html'
    context_object_name = 'task'


class task_edit(generic.UpdateView):
    model = Problem
    template_name = 'task/edit.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('task_list')


class task_delete(generic.DeleteView):
    model = Problem
    template_name = 'task/delete.html'
    success_url = reverse_lazy('task_list')

class ProblemModificationForm(forms.ModelForm):
     class Meta:
         model = ProblemModification
         fields = '__all__'

def mod_task_edit(request, pk):
    post = get_object_or_404(ProblemModification, pk=pk)
    if request.method == "POST":
        form = ProblemModificationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(request.POST['next'], pk=post.pk)
    else:
        form = ProblemModificationForm(instance=post)

    return render(request, 'task/mod_edit.html', {'form': form, 'next': request.GET['next']})


def mod_task_delete(request, pk):
    post = get_object_or_404(ProblemModification, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect(request.POST['next'], pk=post.pk)
    else:
        form = ProblemModificationForm(instance=post)

    return render(request, 'task/mod_delete.html', {'post': post, 'next': request.GET['next']})

def tags(request):
    obj = TagProblem.objects.all()
    pr = Problem.objects.all()
    tg = Tag.objects.all()

    tw = len(Tag.objects.all()) + 1
    problems = []
    for i in range(1, 10):
        problems.append([0] * tw)

    problem_mods = []
    for i in range(1, 10):
        problem_mods.append([0] * tw)

    for ob in obj:
        if ob.problem_modification.name == 'default':
            problems[ob.problem.id][ob.tag.id] = ob.weight
        else:
            problem_mods[ob.problem_modification.id][ob.tag.id] = ob.weight

    return render(request, 'task/tags.html', {'problems': problems, 'mods': problem_mods, 'pr': pr, 'tg': tg})
