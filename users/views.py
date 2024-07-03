from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.views.generic import CreateView, FormView
import random
from django.contrib.auth.hashers import make_password


class RegisterView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_verified = False
        user.save()
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        return response


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None and user.is_verified:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class PasswordResetView(FormView):
    template_name = 'users/password_reset.html'
    form_class = PasswordResetForm

    def form_valid(self, form):
        try:
            user = get_user_model().objects.get(email=form.cleaned_data['email'])
            if user.is_verified:
                new_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=8))
                user.password = make_password(new_password)
                user.save()
                send_mail(
                    'Password Reset',
                    f'Your new password is: {new_password}',
                    'from@example.com',
                    [form.cleaned_data['email']],
                    fail_silently=False,
                )
            else:
                return super().form_invalid(form)
        except get_user_model().DoesNotExist:
            return super().form_invalid(form)

        return super().form_valid(form)