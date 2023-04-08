from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .filters import TaskFilter


class MainTask(ListView):
    model = TaskDay
    paginate_by = 10
    template_name = 'planner/main.html'
    context_object_name = 'tasks'


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TaskFilter(self.request.GET, queryset.filter(user=self.request.user.id))
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['filterset'] = self.filterset
        context['h1'] = 'Планировщик задач'
        return context


class CreateTask(CreateView):
    model = TaskDay
    form_class = AddTaskForm
    template_name = 'planner/create_task.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form is invalid((((((...")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h1'] = 'Добавить задачу'
        return context

    def get_success_url(self):
        return reverse_lazy('planner_main')


class DetailTask(DetailView):
    model = TaskDay
    template_name = 'planner/detail_task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['times'] = TimeDay.objects.filter(task_id=self.kwargs['pk'])
        context['h1'] = 'Задача'
        return context


class DeleteTask(DeleteView):
    model = TaskDay
    template_name = 'planner/delete_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['h1'] = 'Удалить задачу'
        return context

    def get_success_url(self):
        return reverse_lazy('planner_main')


class EditTask(UpdateView):
    model = TaskDay
    template_name = 'planner/edit_task.html'
    form_class = EditTaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['h1'] = 'Редактировать задачу'
        return context


class AddTime(CreateView):
    model = TimeDay
    form_class = AddTimeForm
    template_name = 'planner/add_time.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task_id = self.kwargs['pk']
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form is invalid((((((...")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h1'] = 'Добавить время'
        return context

    def get_success_url(self):
        print(self.kwargs['pk'])
        return reverse_lazy('task_detail', args=(self.kwargs['pk'],))


class DeleteTime(DeleteView):
    model = TimeDay
    template_name = 'planner/delete_time.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои планы'
        context['h1'] = 'Удалить время'
        return context

    def get_success_url(self):
        return reverse_lazy('task_detail', args=(self.object.task_id,))


def add_tomato(request, pk=None):
    task = TaskDay.objects.get(id=pk)
    if task.tomatoes_done:
        task.tomatoes_done += 1
    else:
        task.tomatoes_done = 1
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
