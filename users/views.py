from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserLoginForm
from .models import Profile
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = '/'
    

    def form_valid(self, form):
        response = super().form_valid(form)

        Profile.objects.create(user=self.object)

        login(self.request, self.object)

        return response
    

class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = True

    success_url = '/'


def user_logout(request):
    logout(request)
    return redirect('main_page')


# def user_profile(request):
#     streak_message = None
#     if request.user.profile.streak <= 10:
#         streak_message = "Только начало, все впереди!"
#     elif request.user.profile.streak <= 35:
#         streak_message = "Уже внедрил в свою жизнь продуктивность!"
#     else:
#         streak_message = "БОГ ПРОДУКТИВНОСТИ!"
        
#     return render(request, "users/profile.html", {"user": request.user, "streak_message": streak_message})


class UserProfileView(DetailView):
    template_name  = "users/profile.html"
    model = Profile

    def get_object(self):
        return self.request.user.profile


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        streak = self.object.streak
        streak_message = None

        if streak <= 10:
            streak_message = "Только начало, все впереди!"
        elif streak <= 35:
            streak_message = "Уже внедрил в свою жизнь продуктивность!"
        else:
            streak_message = "БОГ ПРОДУКТИВНОСТИ!"

        context['streak_message'] = streak_message
        context['user'] = self.request.user

        return context
