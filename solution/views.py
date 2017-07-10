from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class solution_list(generic.ListView):
    template_name = 'solution/list.html'
    context_object_name = 'solution'

    def get_queryset(self):
        """Возвращает все решения отсортированные по убыванию времени отправки"""
        return Solution.objects.order_by('-time')


class solution_details(generic.DetailView):
    model = Solution
    template_name = 'solutions/detail.html'


def solution_delete(request, solution_id):
    solution = get_object_or_404(Solution, pk=solution_id)
    try:
        Solution.objects.filter(id=solution_id).delete()
    except ():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'), {'id' : solution_id, 'message' : 'Ошибка'})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'),
                                    {'id': solution_id, 'message': 'Удаление успешно'})