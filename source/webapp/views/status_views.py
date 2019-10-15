from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.models import Tracker, Type, Status
from webapp.forms import TrackerForm, TypeForm, StatusForm


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

def statuses_edit_view(request, pk):
    statuses = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={'status' : statuses.status})
        return render(request, 'update_status.html', context={'form': form, 'status': statuses})
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            statuses.status = request.POST.get('status')
            statuses.save()
            return redirect('status_ls')
        else:
            return render(request, 'update_status.html', context={'status': statuses, 'form': form})
    return redirect('status_ls')


def statuses_delete_view(request, pk):
    statuses = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_status.html', context={'status': statuses})
    elif request.method == 'POST':
        statuses.delete()
        return redirect('status_ls')