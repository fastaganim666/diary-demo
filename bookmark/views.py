from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class MainBookmark(FormView, ListView):
    model = Bookmark
    paginate_by = 10
    template_name = 'bookmark/main.html'
    form_class = AddBookmarkForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user.id
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmarks'] = Bookmark.objects.filter(user=User.objects.get(id=self.request.user.id))
        context['categories'] = Category.objects.filter(user=User.objects.get(id=self.request.user.id))
        context['active_category'] = 'Все закладки'
        context['title'] = 'Приложение закладки'
        context['h1'] = 'Закладки'
        return context

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

    def get_success_url(self):
        return reverse_lazy('bookmark_main')


class EditBookmark(UpdateView):
    model = Bookmark
    form_class = UpdateBookmarkForm
    template_name = 'bookmark/edit_bookmark.html'

    def get_success_url(self):
        return reverse_lazy('bookmark_main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context['title'] = 'Редактирование закладки'
        context['h1'] = 'Редактирование закладки'
        return context


class DeleteBookmark(DeleteView):
    model = Bookmark
    template_name = 'bookmark/delete_bookmark.html'
    success_url = reverse_lazy('bookmark_main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h1'] = 'Удаление закладки'
        return context


class CategoryBookmark(ListView):
    model = Bookmark
    paginate_by = 10
    template_name = 'bookmark/category.html'

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['bookmarks'] = Bookmark.objects.filter(user=User.objects.get(id=self.request.user.id),
                                                       category_id=self.kwargs['pk'])
        context['categories'] = Category.objects.filter(user=User.objects.get(id=self.request.user.id))
        context['h1'] = 'Закладки'
        if len(context['bookmarks']) != 0:
            category = context['bookmarks'][0]
            context['title'] = category.category.name
        else:
            context['title'] = 'Пусто'
        return context

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

    def get_success_url(self):
        return reverse_lazy('bookmark_main')


class AddCategory(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'bookmark/create_category.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(user=User.objects.get(id=self.request.user.id))
        context['h1'] = 'Редактирование категорий закладок'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user.id
        return kwargs


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'bookmark/delete_category.html'
    success_url = reverse_lazy('bookmark_main')

    def get_success_url(self):
        return reverse_lazy('category_add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h1'] = 'Удаление категории'
        return context
