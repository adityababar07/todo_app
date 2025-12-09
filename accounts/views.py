from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from todo.models import ToDo

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'profile_user'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user_posts'] = ToDo.objects.filter(author=user).order_by('-date')
        context['post_count'] = context['user_posts'].count()
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'profile_edit.html'
    fields = ['profile_image', 'username', 'name', 'age', 'bio', 'email',
              'standard', 'division', 'house', 'stream', 'school']
    login_url = 'login'


from django.shortcuts import redirect
from .models import Follow

def follow_user(request, pk):
    user_to_follow = get_object_or_404(CustomUser, pk=pk)
    if request.user == user_to_follow:
        return redirect('profile', pk=pk)
    
    follow_instance = Follow.objects.filter(follower=request.user, following=user_to_follow)
    
    if follow_instance.exists():
        follow_instance.delete()
    else:
        Follow.objects.create(follower=request.user, following=user_to_follow)
        
    return redirect('profile', pk=pk)
