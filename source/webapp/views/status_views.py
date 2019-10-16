from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.models import Status
from webapp.forms import StatusForm
from webapp.views import UpdateView, DeleteView


class StatusView(ListView):
    context_object_name = 'statuses'
    model = Status
    template_name = 'status/status_ls.html'


class StatusCreateView(CreateView):
    template_name = 'status/create_status.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_ls')


class StatusesUpdateView(UpdateView):
    model = Status
    template_name = 'status/update_status.html'
    form_class = StatusForm
    context_key = 'status'

    def get_redirect_url(self):
        return reverse('status_ls')


class StatusesDeleteView(DeleteView):
    template_name = 'status/delete_status.html'
    model = Status
    context_key = 'status'
    confirm_deletion = True

    def get_redirect_url(self):
        return reverse('status_ls')