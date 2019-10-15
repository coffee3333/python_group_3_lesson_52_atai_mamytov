from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView

from webapp.models import Tracker
from webapp.forms import TrackerForm
from webapp.views.update_view import UpdateView


class IndexView(ListView):
    context_object_name = 'trackers'
    model = Tracker
    template_name = 'index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class TaskTrackerView(DetailView):
    template_name = 'TaskTrack.html'
    context_key = 'tracker'
    model = Tracker
    key_kwarg = 'pk'


class TaskTrackerCreateView(CreateView):
    template_name = 'create.html'
    model = Tracker
    form_class = TrackerForm

    def get_success_url(self):
        return reverse('task_track', kwargs={'pk': self.object.pk})


class TaskTrackerUpdateView(UpdateView):
    model = Tracker
    template_name = 'update.html'
    form_class = TrackerForm
    context_key = 'task_tracker'

    def get_redirect_url(self):
        return reverse('task_track', kwargs={'pk': self.object.pk})


class TaskTrackerDeleteView(View):
    def get(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        context = {'task_tracker': task_tracker}
        return render(request, 'delete.html', context)

    def post(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        task_tracker.delete()
        return redirect('index')

    def get_odject(self, pk):
        task_tracker = get_object_or_404(Tracker, pk = pk)
        return task_tracker



