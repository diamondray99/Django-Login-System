from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import *
from .forms import UserForm, ProfileForm


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('HomeView')
    template_name = 'registration/Registration.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profile_update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been Successfully updated')
            return HttpResponseRedirect(reverse_lazy('ProfileView'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form,
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = reverse_lazy('HomeView')


def index(request):
    return render(request, template_name='index.html')