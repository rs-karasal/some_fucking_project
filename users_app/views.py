from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.shortcuts import redirect


from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm


class RegisterView(FormView):
    template_name = 'users_app/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages_app:home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your account has been created successfully.')
        return super().form_valid(form)


class ProfileUpdateView(FormView):
    template_name = 'users_app/profile_update.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile_update')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'users_app/login.html'
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('pages_app:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'You have been logged in successfully.')
        else:
            messages.error(self.request, 'Invalid username or password.')
        return super().form_valid(form)


class LogoutConformationView(TemplateView):
    template_name = 'users_app/logout.html'
    success_url = reverse_lazy('pages_app:home')

    def post(self, request, *args, **kwargs):
        if 'confirm' in request.POST:
            logout(request)
            return redirect('pages_app:home')
        else:
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        return super().post(request, *args, **kwargs)
