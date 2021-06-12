from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from .forms import CommentForm

from .models import Post, Comment

class HomePageView(TemplateView):
    model = Post
    template_name = 'home.html'

class StudyListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    login_url = 'login'

class StudyDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login'

class StudyCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StudyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class StudyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

def StudyCommentCreateView(request):
    form = CommentForm(request.Post or None)
    if form.is_valid():
        form.save()
    context = {'form':form}
    # success_url = reverse_lazy('post_detail')
    # model = Comment
    # template_name = 'comment_new.html'
    # fields = ['comment', 'author']
    return render(request, 'comments/comment_new.html', context)

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)