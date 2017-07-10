from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class contest_list(generic.ListView):
    template_name = 'contests/list.html'
    context_object_name = 'contest_list'

    def get_queryset(self):
        """Возвращает все архивы, отсортированные по имени"""
        return Archive.objects.order_by('name')


class contest_details(generic.DetailView):
    model = Archive
    template_name = 'contests/detail.html'


class contest_edit(generic.DetailView):
    model = Archive
    template_name = 'contests/edit.html'


def contest_delete(request, contest_id):
    contest = get_object_or_404(Archive, pk=contest_id)
    try:
        Archive.objects.filter(id=contest_id).delete()
    except ():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'), {'id' : contest_id, 'message' : 'Ошибка'})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'),
                                    {'id': contest_id, 'message': 'Удаление успешно'})