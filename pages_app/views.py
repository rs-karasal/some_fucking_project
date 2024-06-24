from django.views.generic import TemplateView
from django.conf import settings


class HomePageView(TemplateView):
    template_name = 'pages_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
