from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.models import Tracker, Type, Status
from webapp.forms import TrackerForm, TypeForm, StatusForm
from webapp.views import UpdateView


class StatusView(ListView):
    context_object_name = 'statuses'
    model = Status
    template_name = 'status_ls.html'


class StatusCreateView(CreateView):
    template_name = 'create_status.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_ls')

class StatusesUpdateView(UpdateView):
    model = Status
    template_name = 'update_status.html'
    form_class = StatusForm
    context_key = 'status'

    def get_redirect_url(self):
        return reverse('status_ls')

def statuses_delete_view(request, pk):
    statuses = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_status.html', context={'status': statuses})
    elif request.method == 'POST':
        statuses.delete()
        return redirect('status_ls')