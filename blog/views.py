from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreate(CreateView):
    model = Blog


class BlogList(ListView):
    model = Blog


class BlogDetail(DetailView):
    model = Blog


class BlogEdit(UpdateView):
    model = Blog


class BlogDelete(DeleteView):
    model = Blog