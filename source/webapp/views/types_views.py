from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.models import Tracker, Type, Status
from webapp.forms import TrackerForm, TypeForm, StatusForm
from webapp.views import UpdateView


class TypeView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'types_ls.html'


class TypesCreateView(CreateView):
    template_name = 'create_type.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_ls')


class TypesUpdateView(UpdateView):
    model = Type
    template_name = 'update_type.html'
    form_class = TypeForm
    context_key = 'type'

    def get_redirect_url(self):
        return reverse('type_ls')


def type_delete_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_type.html', context={'type': type})
    elif request.method == 'POST':
        type.delete()
        return redirect('type_ls')