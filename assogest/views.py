import markdown
import os

from django.conf import settings
from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm

README = os.path.join(settings.BASE_DIR, 'README.md')


def markdown_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        text = file.read()
        return markdown.markdown(text)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['readme'] = markdown_from_file(README)
        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
