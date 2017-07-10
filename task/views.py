from _md5 import md5

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, render_to_response
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from pmanager.settings import BASE_DIR
from .models import *
from django.views import generic


def auth_check(request):
    return request.user.is_authenticated()


class task_list(generic.ListView):
    template_name = 'task/list.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Возвращает все задачи, отсортированные по имени"""
        return Problem.objects.order_by('name')


    def get_context_data(self, **kwargs):
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
    post = ProblemModification.objects.get(pk=pk)

    statement_enc = get_statement(post)  # получение условий из строки или текстового файла
    if request.method == "POST":
        form = ProblemModificationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            statement = request.POST.get('statement')
            if (statement is not None):
                type_st = AttachmentType.objects.filter(name = "Условие").first()
                Attachment.objects.filter(problem_modification=post, type = type_st).\
                    update_or_create(defaults={'text': statement}, problem_modification=post, type = type_st)
        return redirect(request.POST['next'], pk=post.pk)

    else:
        form = ProblemModificationForm(instance=post)

    return render(request, 'task/mod_edit.html', {'BASE_DIR': BASE_DIR, 'form': form, 'statement': statement_enc,'next': request.GET['next']})


def mod_task_copy(request, pk):
    post = get_object_or_404(ProblemModification, pk=pk) #оригинальный пост
    attrs = Attachment.objects.filter(problem_modification=post) #получение дополнений

    post.pk = None
    post.save()  # сохранение копии

    for attr in attrs:  # сохранение копий дополнений
        attr.pk = None
        attr.problem_modification = post
        attr.save()

    return redirect(request.GET['next'], pk=post.pk) #из GET! запроса


def get_statement(post): #получение условий из строки или текстового файла
    try:
        statement = Attachment.objects.get(problem_modification=post, type__name="Условие")
    except Attachment.DoesNotExist:
        statement = None

    if (statement is not None):

        if (statement.contents.name != "" and statement.text == ""):
            statement_file = statement.contents
            statement_file.open(mode='rb')
            statement_text = statement_file.readlines()
            statement_enc = ""
            for line in statement_text:
                statement_enc += line.decode("utf-8")
            statement_file.close()
        else:
            statement_enc = statement.text
    else:
        statement_enc = ""

    return statement_enc


def mod_task_delete(request, pk):
    post = get_object_or_404(ProblemModification, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect(request.POST['next'], pk=post.pk)
    else:
        form = ProblemModificationForm(instance=post)

    return render(request, 'task/mod_delete.html', {'post': post, 'next': request.GET['next']})


def tags(request):
    objects_list = TagProblem.objects.all()
    problems_list = Problem.objects.all()
    modifications_list = ProblemModification.objects.all()
    tags_list = Tag.objects.order_by('coeff', 'name').all()  #сортировка по коэффициенту и имени

    tw = len(Tag.objects.all()) + 1
    problems = []
    for i in range(len(problems_list) + 1):
        problems.append([0] * tw)

    problem_mods = []
    for i in range(len(modifications_list) + 1):
        problem_mods.append([0] * tw)

    for index, tl in enumerate(tags_list):
        for ob in objects_list:
            if tl == ob.tag:
                if ob.problem_modification.name == 'default':  #если относится к концепту
                    problems[ob.problem.id][index] = ob.weight
                else:                                          #если относится к модификации
                    problem_mods[ob.problem_modification.id][index] = ob.weight

    return render(request, 'task/tags.html', {'problems': problems, 'mods': problem_mods,
                                              'pr': problems_list, 'tg': tags_list})


class AuthForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username', 'password'}

def sign_in(request):
    error = False
    org_list = User.objects.all().filter(company__is_company=True)
    if request.method == "POST":
        form = AuthForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            userObj = form.cleaned_data
            user_id = userObj['username']
            username = User.objects.get(pk=user_id)
            # password = md5(userObj['password'].encode('utf-8'))
            password = userObj['password']
            user = authenticate(request, username=username, password=password)
            if (user is not None and user.is_active):
                login(request, user)
                return HttpResponseRedirect('/task')
            else:
                error = True

    return render(request, 'task/sign_in.html', {'org_list': org_list, 'error':error})


def lk(request):
    problems_list = Problem.objects.all()
    # modifications_list = ProblemModification.objects.all()

    return render(request, 'task/tags.html', {'pr': problems_list})