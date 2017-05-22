from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic

class user_list(generic.ListView):
    template_name = 'users/list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        """Return all users sort by name"""
        return User.objects.order_by('name')


class user_details(generic.DetailView):
    model = User
    template_name = 'users/detail.html'


class user_edit(generic.DetailView):
    model = User
    template_name = 'users/edit.html'


def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        User.objects.filter(id=user_id).delete()
    except ():
        return render(request, 'users/detail.html', {
            'question': user,
            'message': "Error occured",
        })
    else:
        return render(request, 'users/detail.html', {
            'question': user,
            'message': "Deleted",
        })