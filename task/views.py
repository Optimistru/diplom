from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


class mod_task_edit(generic.UpdateView):
    model = ProblemModification
    template_name = 'task/mod_edit.html'
    fields = '__all__'

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class mod_task_delete(generic.DeleteView):
    model = ProblemModification
    template_name = 'task/mod_delete.html'

