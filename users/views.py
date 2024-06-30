from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.views.generic import CreateView, FormView
import random
from django.contrib.auth.hashers import make_password


from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        return response


class CustomLoginView(LoginView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/login.html'
    success_url = '/'


class PasswordResetView(FormView):
    model = User
    template_name = 'users/password_reset.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        """Проверка наличия пользователя с указанным адресом электронной почты"""
        try:
            user = User.objects.get(email=form.cleaned_data['email'])
        except User.DoesNotExist:
            """Обработка случая, когда пользователь не найден"""
            return super().form_invalid(form)

        """Генерация нового пароля"""
        new_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=8))
        user.password = make_password(new_password)
        user.save()

        """Отправка сообщения о смене пароля"""
        send_mail(
            'Password Reset',
            f'Your new password is: {new_password}',
            'from@example.com',
            [form.cleaned_data['email']],
            fail_silently=False,
        )

        return super().form_valid(form)