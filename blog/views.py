from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog
from users.models import User


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogList(ListView):
    model = Blog


class BlogDetail(DetailView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count += 1
        self.object.save()
        return self.object



class BlogEdit(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/user_form'
    success_url = reverse_lazy('mail:user_list.html')
    permission_required = 'users.set_active'
    fields = ['is_active', ]


def users(request):
    context = {
        'user_list': User.objects.all()
    }
    return render(request, 'mail/user_list.html', context)




