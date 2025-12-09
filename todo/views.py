from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404


# from .forms import CommentForm

from .models import ToDo, Comment


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Get users the current user follows
            following_users = self.request.user.following.values_list('following', flat=True)
            # Filter posts by followed users OR the current user
            context['feed_posts'] = ToDo.objects.filter(
                author__in=list(following_users) + [self.request.user.id]
            ).order_by('-date')
            
            # Get suggestions (users not followed and not self)
            from accounts.models import CustomUser
            context['suggestions'] = CustomUser.objects.exclude(
                id__in=list(following_users) + [self.request.user.id]
            )[:5]
            context['suggestions'] = CustomUser.objects.exclude(
                id__in=list(following_users) + [self.request.user.id]
            )[:5]
        else:
            from django.contrib.auth.forms import AuthenticationForm
            context['form'] = AuthenticationForm()
        return context


class StudyListView(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = 'todo_list.html'
    login_url = 'login'


class StudyDetailView(LoginRequiredMixin, DetailView):
    model = ToDo
    template_name = 'todo_detail.html'
    login_url = 'login'


from .forms import TodoForm

class StudyCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    template_name = 'todo_new.html'
    form_class = TodoForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ToDo
    template_name = 'todo_edit.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class StudyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ToDo    
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class StudyCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments/comment_new.html'
    fields = ['comment']
    success_url = reverse_lazy('todo_list')
    login_url = 'login'
    
    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        # form.instance.todo_id = self.kwargs['pk']
        return super().form_valid(form)
        # return render(request, 'comments/comment_new.html', context)

